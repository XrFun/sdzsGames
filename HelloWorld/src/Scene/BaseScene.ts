/**
 * Created by youmo on 2017/2/17.
 */
/**
 * 这是一个 Scene 基类所有公共方法都抽象都这个类里面实现.
 */
class BaseScene extends egret.DisplayObjectContainer {
    public stageW: number = egret.MainContext.instance.stage.stageWidth;
    public stageH: number = egret.MainContext.instance.stage.stageHeight;
    public currentScene: egret.DisplayObjectContainer;

    public changeScene(scene: egret.DisplayObjectContainer) {
        if (this.currentScene) {
            this.stage.removeChild(this.currentScene);
        }
        this.currentScene = scene;
        this.stage.addChild(this.currentScene);
    }

    public getCurrentScene() {
        return this.currentScene;
    }

    public createBitmapByName(name: string) {
        let result = new egret.Bitmap();
        let texture: egret.Texture = RES.getRes(name);
        result.texture = texture;
        return result;
    }

    public getStage() {
        return this.stage;
    }
}