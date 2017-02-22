/**
 * Created by youmo on 2017/2/17.
 */

/**
 * 敌人类,BOSS系文哥.
 */
class Entity extends egret.Sprite {
    public enemyMC : egret.MovieClip;
    public mcDataFactory :　egret.MovieClipDataFactory;　
    public constructor(enemyType:number) {
        super();
        this.init(enemyType);
    }

    private init(enemyType):void {
      //加载enemy 行走的动画****************
      var data = RES.getRes("hero"+ enemyType + "_json");
      var texture = RES.getRes("hero"+ enemyType + "_png");
      this.mcDataFactory = new egret.MovieClipDataFactory(data, texture);
      this.enemyMC = new egret.MovieClip(this.mcDataFactory.generateMovieClipData("walk"));
      this.addChild(this.enemyMC);
      this.enemyMC.play(-1);
    }
}