import api from '@/helpers/axios-wrapper.ts'
import { TEST_PREFIX } from '@/api/config.ts'

export default {
  baseAuthUrl: `/${TEST_PREFIX}`,
  async callExemple() {
    return await api.get(`${this.baseAuthUrl}`, { "cors": "no" })
  }
  // async functionExemple2() {
  //   return await api.post(`${this.baseAuthUrl}/<route_name>`, {})
  // },
  // async functionExemple3() {
  //   return await api.put(`${this.baseAuthUrl}/<route_name>`, {})
  // },
  // async functionExemple4() {
  //   return await api.delete(`${this.baseAuthUrl}/<route_name>/<id>`)
  // }
}
