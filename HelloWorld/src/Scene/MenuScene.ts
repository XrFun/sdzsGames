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
        let icon = this.createBitmapByName("egret_icon_png");
        this.addChild(icon);
        icon.x = 26;
        icon.y = 33;
    }
}