# This file is used to initialize the deployment

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = "{{ cookiecutter.gcloud_project }}"
}

resource "google_sql_database_instance" "instance" {
  name             = "{{ cookiecutter.project_slug.replace('_', '-') }}-instance"
  project          = "{{cookiecutter.gcloud_project}}"
  region           = "{{ cookiecutter.gcloud_region }}"
  database_version = "POSTGRES_15"
  settings {
    tier = "db-f1-micro"
  }

  deletion_protection = "true"
}

resource "google_sql_database" "database" {
  name     = "{{cookiecutter.project_slug}}_db"
  instance = google_sql_database_instance.instance.name
}

resource "google_sql_user" "updated_user" {
  name     = "postgres"
  instance = google_sql_database_instance.instance.name
  password = "postgres"
}

resource "google_artifact_registry_repository" "cookiecutter-repo" {
  location      = "{{cookiecutter.gcloud_region}}"
  repository_id = "cookiecutter-template"
  description   = "Repository for cookiecutter template generation"
  format        = "DOCKER"
}

resource "null_resource" "build_push_image" {
  provisioner "local-exec" {
    command = <<-EOT
      gcloud auth configure-docker
      docker build --platform linux/amd64 -t "europe-docker.pkg.dev/{{ cookiecutter.gcloud_project }}/cookiecutter-template/{{ cookiecutter.project_slug.replace('_', '-') }}" -f Dockerfile.prod .
      docker push "europe-docker.pkg.dev/{{ cookiecutter.gcloud_project }}/cookiecutter-template/{{ cookiecutter.project_slug.replace('_', '-') }}"
    EOT
  }
}

resource "google_cloud_run_service" "backend_service" {
  name     = "{{ cookiecutter.project_slug.replace('_', '-') }}"
  location = "{{ cookiecutter.gcloud_region }}"

  template {
    spec {
      containers {
        image = "europe-docker.pkg.dev/{{ cookiecutter.gcloud_project }}/cookiecutter-template/{{ cookiecutter.project_slug.replace('_', '-') }}"
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale"      = "1000"
        "run.googleapis.com/cloudsql-instances" = google_sql_database_instance.instance.connection_name
        "run.googleapis.com/client-name"        = "terraform"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  depends_on = [null_resource.build_push_image]
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location = google_cloud_run_service.backend_service.location
  project  = google_cloud_run_service.backend_service.project
  service  = google_cloud_run_service.backend_service.name

  policy_data = data.google_iam_policy.noauth.policy_data
}

resource "google_secret_manager_secret" "backend_secret" {
  secret_id = "{{ cookiecutter.project_slug.replace('_', '-') }}"

  replication {
    automatic = true
  }
}

