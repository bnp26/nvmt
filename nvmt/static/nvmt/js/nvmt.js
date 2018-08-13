var ctx = $('#demoCanvas')[0].getContext('2d');
var windowWidth = window.innerWidth;
var windowHeight = window.innerHeight;
ctx.canvas.width = windowWidth;
ctx.canvas.height = windowHeight;

/*

==============================
CARDS FOR TEST
==============================

*/

const cards = {
card_1 : [
  {'x':9, 'y':12, 'is_goal': false},
  {'x':17, 'y':12, 'is_goal': false},
  {'x':25, 'y':12, 'is_goal': false},
  {'x':33, 'y':12, 'is_goal': false},
  {'x':41, 'y':12, 'is_goal': false},
  {'x':25, 'y':7, 'is_goal': false},
  {'x':25, 'y':16, 'is_goal': false},
  {'x':25, 'y':20, 'is_goal': true},
  {'x':25, 'y':24, 'is_goal': false}
],
card_2 : [
  {'x':2, 'y':15, 'is_goal': false},
  {'x':16, 'y':14, 'is_goal': false},
  {'x':9, 'y':29, 'is_goal': false},
  {'x':24, 'y':21, 'is_goal': false},
  {'x':28, 'y':2, 'is_goal': false},
  {'x':32, 'y':6, 'is_goal': false},
  {'x':41, 'y':4, 'is_goal': false},
  {'x':40, 'y':15, 'is_goal': true},
  {'x':47, 'y':11, 'is_goal': false},
  {'x':45, 'y':25, 'is_goal': false}
],
card_3 : [
  {'x':5, 'y':5, 'is_goal': false},
  {'x':13, 'y':2, 'is_goal': false},
  {'x':17, 'y':25, 'is_goal': false},
  {'x':21, 'y':12, 'is_goal': false},
  {'x':29, 'y':12, 'is_goal': false},
  {'x':21, 'y':29, 'is_goal': true},
  {'x':29, 'y':29, 'is_goal': false},
  {'x':33, 'y':25, 'is_goal': false},
  {'x':38, 'y':2, 'is_goal': false},
  {'x':45, 'y':5, 'is_goal': false}
],
card_4 : [
  {'x':2, 'y':4, 'is_goal': false},
  {'x':19, 'y':5, 'is_goal': true},
  {'x':17, 'y':12, 'is_goal': false},
  {'x':34, 'y':11, 'is_goal': false},
  {'x':41, 'y':16, 'is_goal': false},
  {'x':4, 'y':27, 'is_goal': false},
  {'x':23, 'y':26, 'is_goal': false},
  {'x':47, 'y':17, 'is_goal': false},
  {'x':47, 'y':29, 'is_goal': false},
  {'x':49, 'y':11, 'is_goal': false}
],
card_5 : [
  {'x':25, 'y':5, 'is_goal': false},
  {'x':16, 'y':13, 'is_goal': false},
  {'x':25, 'y':15, 'is_goal': false},
  {'x':34, 'y':13, 'is_goal': false},
  {'x':8, 'y':19, 'is_goal': false},
  {'x':14, 'y':21, 'is_goal': true},
  {'x':25, 'y':21, 'is_goal': false},
  {'x':36, 'y':21, 'is_goal': false},
  {'x':42, 'y':19, 'is_goal': false},
  {'x':25, 'y':29, 'is_goal': false}
],
card_6 : [
  {'x':6, 'y':7, 'is_goal': false},
  {'x':12, 'y':12, 'is_goal': false},
  {'x':5, 'y':19, 'is_goal': false},
  {'x':9, 'y':26, 'is_goal': false},
  {'x':16, 'y':27, 'is_goal': false},
  {'x':25, 'y':14, 'is_goal': false},
  {'x':31, 'y':6, 'is_goal': false},
  {'x':40, 'y':9, 'is_goal': true},
  {'x':44, 'y':21, 'is_goal': false},
  {'x':44, 'y':29, 'is_goal': false}
],
card_7 : [
  {'x':13, 'y':6, 'is_goal': false},
  {'x':10, 'y':12, 'is_goal': false},
  {'x':16, 'y':14, 'is_goal': true},
  {'x':16, 'y':21, 'is_goal': false},
  {'x':11, 'y':30, 'is_goal': false},
  {'x':24, 'y':17, 'is_goal': false},
  {'x':35, 'y':14, 'is_goal': false},
  {'x':41, 'y':4, 'is_goal': false},
  {'x':29, 'y':14, 'is_goal': false},
  {'x':37, 'y':24, 'is_goal': false}
],
card_8 : [
  {'x':4, 'y':4, 'is_goal': false},
  {'x':11, 'y':9, 'is_goal': false},
  {'x':9, 'y':13, 'is_goal': false},
  {'x':15, 'y':18, 'is_goal': false},
  {'x':20, 'y':5, 'is_goal': false},
  {'x':26, 'y':20, 'is_goal': false},
  {'x':35, 'y':22, 'is_goal': false},
  {'x':39, 'y':26, 'is_goal': true},
  {'x':47, 'y':24, 'is_goal': false}
],
card_9 : [
  {'x':7, 'y':10, 'is_goal': false},
  {'x':12, 'y':5, 'is_goal': false},
  {'x':18, 'y':9, 'is_goal': true},
  {'x':15, 'y':18, 'is_goal': false},
  {'x':9, 'y':25, 'is_goal': false},
  {'x':24, 'y':17, 'is_goal': false},
  {'x':14, 'y':34, 'is_goal': false},
  {'x':39, 'y':15, 'is_goal': false},
  {'x':39, 'y':24, 'is_goal': false},
  {'x':41, 'y':29, 'is_goal': false}
]}

function finishedTest(trial) {
  console.log(trial);
}

function onTargetClick(event, data) {
  let rect = new createjs.Shape();
  let stage = data.trial.stage;
  let oldRect = this.rect;
  let completed = false;
  if (this.is_target) {
     this.clicked = data.timer.getTimeValues();
     data.timer.stop();
     stage.removeChild(this.rect);
     rect.graphics.f("#16a2e0").dr(oldRect.graphics.command.x, oldRect.graphics.command.y, oldRect.graphics.command.w, oldRect.graphics.command.h);
     data.trial.pop();
     stage.addChild(rect);
     stage.update();
     this.rect = rect;
     completed = true;
   }
   else {
     this.clicked = data.timer.getTimeValues();
     stage.removeChild(this.rect);
     rect.graphics.f("#004d40").dr(oldRect.graphics.command.x, oldRect.graphics.command.y, oldRect.graphics.command.w, oldRect.graphics.command.h);
     stage.addChild(rect);
     this.rect = rect;
     stage.update();
   }

   if (completed) {
     stage.removeAllChildren();
     if (data.trial.cards !== null) {
       let tempTimer = new Timer();
       tempTimer.start({countdown: true, startValues: {seconds: 1}});
       tempTimer.addEventListener('targetAchieved', function (e){
         data.trial.draw();
         stage.update();
       });
     } else {
       finishedTest(data.trial);
     }
   }
}

class Target {
  constructor(x, y, is_target) {
    this.x = x;
    this.y = y;
    this.is_target = is_target;
    this.clicked = null;
    // get the size of the canvas with respect to the window.
    this.rect = new createjs.Shape();
  }
}

class Card {
  constructor(targets, trial) {
    this.targets = [];
    this.next = null;
    this.trial = trial;
    var timer = new Timer();
    this.timer = timer;
    if (targets !== null) {
      for (let target of targets) {
        var newTarget = new Target(target.x, target.y, target.is_goal);
        newTarget.rect.on("click", onTargetClick, newTarget, false, {timer: timer, trial:this.trial});
        this.targets.push(newTarget);
      }
    }
  }

  start() {
    this.timer.start({precision: 'secondTenths'});
  }
}

class Trial {
  constructor(trial_num, stage) {
    this.trial_num = trial_num;
    this.stage = stage;
    this.cards = null;
    this.finishedCards = [];
    // adding cards in the cards dictionary to the trial
    for (let card of Object.keys(cards)) {
      if (this.cards === null) {
        this.cards = new Card(cards[card], this);
      } else {
        let current = this.cards;
        while (current.next !== null) {
          current = current.next;
        }
        current.next = new Card(cards[card], this);
      }
    }
  }

  pop () {
    let cardToPop = this.cards;
    this.cards = this.cards.next;
    this.finishedCards.push(cardToPop);
    return cardToPop;
  }

  draw () {
    var ctx = $('#demoCanvas')[0].getContext('2d');
    var windowWidthScale = ctx.canvas.width / 50;
    var windowHeightScale = ctx.canvas.height / 35;

    let card = this.cards;
    for (let target of card.targets) {
      let rect = target.rect;
      let sizeScale = Math.max(windowWidthScale, windowHeightScale);
      rect.graphics.beginFill("#26a69a").dr(target.x * windowWidthScale, target.y * windowHeightScale, sizeScale*1.25, sizeScale*1.25);
      this.stage.addChild(rect);
    }
    card.start();
  }
}

var ctx = $('#demoCanvas')[0].getContext('2d');
var windowWidthScale = ctx.canvas.width / 50;
var windowHeightScale = ctx.canvas.height / 35;

function init() {
  var stage = new createjs.Stage("demoCanvas");
  createjs.Touch.enable(stage);
  // stage.
  // instructions text
  let instructions_main = new createjs.Text("Welcome to the Poreh Non-Verbal Memory Test", "40px Arial", "#009688");
  instructions_main.name = "instructionsText";
  instructions_main.textAlign = "center";
  instructions_main.x = 25 * windowWidthScale;
  instructions_main.y = 15 * windowHeightScale - 120;

  let instructions_sub = new createjs.Text("click below to Start", "18px Arial", "#009688");
  instructions_sub.name = "instructionsText";
	instructions_sub.textAlign = "center";
  instructions_sub.x = 25 * windowWidthScale;
	instructions_sub.y = 15 * windowHeightScale;

  // background of start button
  var background = new createjs.Shape();
	background.name = "background";
	background.graphics.beginFill("#FF5722").drawRoundRect(0, 0, 150, 60, 10);
  // text of start button
  let label = new createjs.Text("Start", "30px Arial", "#000000");
  label.name = "instructionsText";
	label.textAlign = "center";
	label.textBaseline = "middle";
  label.x = 150/2;
  label.y = 60/2;
  // creating button
  var button = new createjs.Container();
	button.name = "button";
	button.x = 23.1 * windowWidthScale;
	button.y = 16 * windowHeightScale;
	button.addChild(background, label);

  button.addEventListener("click", function (event){
    stage.removeAllChildren();
    beginTrial(stage);
  });
  // adding button to stage.
  stage.addChild(instructions_main, instructions_sub, button);

  function beginTrial(stage) {
    var current_trial = 1;
    var trial = new Trial(current_trial, stage);
    console.log("starting test");
    trial.draw(stage);
    stage.update();
  }

  /*for (let i = 0; i < trial.cards[0].targets.length; i++) {
   let rect = new createjs.Shape();
   rect.graphics.beginFill("green").dr(trial.cards[0].targets[i].x * windowWidthScale, trial.cards[0].targets[i].y * windowHeightScale, 35, 35);
   stage.addChild(rect);
  }
  for (let i = 0; i < 10; i++) {
   let rect = new createjs.Shape();
   rect.graphics.beginFill("green").dr(60 * i + 25, 60, 50, 50);
   stage.addChild(rect);
  }*/

  stage.update();
}