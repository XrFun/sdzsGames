/**
 * Created by youmo on 2017/2/17.
 */
/**
 * 菜单场景
 */
class MenuScene extends BaseScene {
    public constructor() {
        super();
        this.init();
    }

    private init() {
        let bg = this.createBitmapByName("menu_bg_jpg");
        this.addChild(bg);

        let startBtn = this.createBitmapByName("start_png");
        this.addChild(startBtn);
        startBtn.anchorOffsetX = startBtn.width / 2;
        startBtn.anchorOffsetY = startBtn.height / 2;
        startBtn.x = this.stageW * .4;
        startBtn.y = this.stageH * .7;
        startBtn.addEventListener(egret.TouchEvent.TOUCH_TAP,this.startGame,this);
        startBtn.touchEnabled = true;
    }

    private startGame(evt:egret.TouchEvent){
        let scene = new FightScene();
        this.changeScene(scene);
    }
}