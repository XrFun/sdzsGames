var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
/**
 * Created by youmo on 2017/2/17.
 */
/**
 * 战斗场景
 */
var FightScene = (function (_super) {
    __extends(FightScene, _super);
    function FightScene() {
        return _super.apply(this, arguments) || this;
    }
    return FightScene;
}(BaseScene));
__reflect(FightScene.prototype, "FightScene");
//# sourceMappingURL=FightScene.js.map