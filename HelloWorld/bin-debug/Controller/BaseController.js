/**
 * Created by youmo on 2017/2/17.
 */
var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
/**
 * 这是一个 controller 基类所有公共方法都抽象都这个类里面实现.
 */
var BaseController = (function (_super) {
    __extends(BaseController, _super);
    function BaseController() {
        return _super.apply(this, arguments) || this;
    }
    return BaseController;
}(egret.DisplayObjectContainer));
__reflect(BaseController.prototype, "BaseController");
//# sourceMappingURL=BaseController.js.map