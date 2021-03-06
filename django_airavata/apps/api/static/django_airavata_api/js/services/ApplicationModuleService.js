
import ApplicationDeploymentDescription from '../models/ApplicationDeploymentDescription'
import ApplicationModule from '../models/ApplicationModule'
import FetchUtils from '../utils/FetchUtils'

class ApplicationModuleService {
    list(data = null) {
        if (data) {
            return Promise.resolve(data.map(result => new ApplicationModule(result)));
        } else {
            return FetchUtils.get('/api/applications/')
                .then(json => json.map(result => new ApplicationModule(result)));
        }
    }

    create(project) {
        // TODO
    }

    update() {
        // TODO
    }

    get(appModuleId) {
        return FetchUtils.get('/api/applications/' + encodeURIComponent(appModuleId) + '/')
            .then(json => new ApplicationModule(json));
    }

    getApplicationDeployments(appModuleId) {
        return FetchUtils.get('/api/applications/' + encodeURIComponent(appModuleId) + '/application_deployments/')
            .then(json => json.map(result => new ApplicationDeploymentDescription(result)));
    }
}

// Export as a singleton
export default new ApplicationModuleService();