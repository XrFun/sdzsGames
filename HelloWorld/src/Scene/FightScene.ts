/**
 * Created by youmo on 2017/2/17.
 */
/**
 * 战斗场景
 */
class FightScene extends BaseScene {
    public constructor() {
        super();
        this.init();
    }

    private init() {
        let sky = this.createBitmapByName("bg_jpg");
        this.addChild(sky);
        let stageW = this.stage.stageWidth;
        let stageH = this.stage.stageHeight;
        sky.width = stageW;
        sky.height = stageH;
    }
}