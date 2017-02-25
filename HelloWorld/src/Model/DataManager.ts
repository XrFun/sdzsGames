/**
 * Created by youmo on 2017/2/17.
 */
/**
 * 数据管理器,暂时创建一个
 */
class DataManager {
    public _map_data;

    private init() {
        this.loadConfig();
    }

    private parseConfigData(data, func) {
        if (data && data.list.length > 0) {
            var dicInfo = {};
            for (var idx = 0; idx < data.list.length; ++idx) {
                var vo = data.list[idx];
                if (func) {
                    vo.id = func(vo);
                }
                dicInfo[vo.id] = vo;
            }
            return {dic: dicInfo, arr: data.list};
        }
        return {};
    }

    private loadConfig() {
        RES.getResByUrl("resource/config/base_way.json", this.testCallBack, this);
    }

    private testCallBack(data, key) {
        // TODO log
        //GameConst.logObject(data);
        this._map_data = this.parseConfigData(data);
    }

    public getMapConfigData() {
        return this._map_data;
    }
}

var _vipManagerInstance = null;

DataManager.getInstance = function() {
    if (!_vipManagerInstance) {
        _vipManagerInstance = new DataManager();
        _vipManagerInstance.init();
    }
    return _vipManagerInstance;
};