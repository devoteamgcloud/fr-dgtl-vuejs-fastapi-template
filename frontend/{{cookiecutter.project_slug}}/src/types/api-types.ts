type StatusCode = 200 | 201 | 204 | 400 | 401 | 403 | 404 | 422 | 500
type SnackLocation = 'top' | 'bottom' | 'left' | 'right' | 'top right' | 'top left' | 'bottom right' | 'bottom left'
type SnackMessageMapping = Partial<Record<StatusCode, string>>

export class SnackBar {
    show?: boolean
    location?: SnackLocation
    mapping?: SnackMessageMapping  // Custom mapping for snackbar text

    constructor(show: boolean = true, location: SnackLocation = 'top right', mapping: SnackMessageMapping = null) {
        this.show = show;
        this.location = location;
        this.mapping = mapping
    }
}