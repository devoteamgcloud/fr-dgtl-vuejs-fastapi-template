import { APISettings } from '@/api/config'
import axios from 'axios'

const axiosInstance = axios.create(APISettings)

export default {
  axiosInstance,
  async get(path: any, params: any, headers = null) {
    const config = {
      method: 'GET',
      url: `${path}`,
      params: params
    }
    if (headers) {
      config['headers'] = headers
    }
    return await axiosInstance(config)
  },
  async post(path: any, payload: any) {
    return await axiosInstance({
      method: 'POST',
      url: `${path}`,
      data: payload
    })
  },
  async patch(path: any, payload: any, headers = {}) {
    const config = { method: 'PATCH', url: `${path}`, data: payload }
    if (Object.keys(headers).length > 0) {
      config['headers'] = headers
    }
    return await axiosInstance(config)
  },
  async put(path: any, payload: any, headers = {}) {
    const config = { method: 'PUT', url: `${path}`, data: payload }
    if (Object.keys(headers).length > 0) {
      config['headers'] = headers
    }
    return await axiosInstance(config)
  },
  async delete(path: any) {
    return await axiosInstance({
      method: 'DELETE',
      url: `${path}`
    })
  }
}
