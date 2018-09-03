/* var ctx = $('#demoCanvas')[0].getContext('2d');
var windowWidth = window.innerWidth;
var windowHeight = window.innerHeight;

// ctx.canvas.width = windowWidth;
// ctx.canvas.height = windowHeight
*/
/*

==============================
CARDS FOR TEST
==============================

*/
/*

var test_data = {
  'trials': []
};

const cards = {
  'sample': {
    width: 187.5,
    height: 93.75,
    points: [
      { x: 48, y: 28, value: '1', next: '2'},
      { x: 75, y: 7, value: '2', next: '3'},
      { x: 88, y: 23, value: '3', next: '4'},
      { x: 70, y: 24, value: '4', next: '5'},
      { x: 78, y: 45, value: '5', next: '6'},
      { x: 20, y: 45, value: '6', next: '7'},
      { x: 17, y: 19, value: '7', next: '8'},
      { x: 45, y: 16, value: '8', next: '-1'}
    ]
  }
}

function sendData() {
  let simplifiedData = {'trials': []};
  for(let trial of test_data.trials) {
    simplifiedData.trials.push(trial.strip());
  }

  let path = window.location.pathname;
  let test_code = path.split('/')[3];
  let url = '/tmt/test-data/' + test_code + '/';
  let csrftoken = $('#demoCanvas input').val();
  var data = stringify(simplifiedData, null, 2);
  $.ajax({
    type: "POST",
    url: url,
    headers: {'X-CSRFToken': csrftoken},
    dataType: 'json',
    data: data,
    success: function (data, textStatus, jqXHR) {
      console.log(data);
      console.log(textStatus);
      console.log(jqXHR);
    },
    fail: function (error) {
      console.log(error);
  }
  });
}

var ismousedown = false;
var linecolor = "#000000";
var madeMistake = false;
function handlePointInteraction(event, data) {
  let sizeScale = Math.max(data.card.windowWidthScale, data.card.windowHeightScale);

  if (event.type == 'mousedown') {
    ismousedown = true;
  }
  else if (event.type == 'mouseup') {
    ismousedown = false;
  }

  if (ismousedown){
    // the user has made a mistake and the current point needs to remove the line it has made
    if (madeMistake && this.nextTarget == data.card.currentTarget && event.type == 'mouseover') {
      let g = new createjs.Graphics().beginStroke("#000000").beginFill("#CDCDCD").dc(5.8, 10, sizeScale*1.2);
      event.target.graphics = g;
    }
    else if ((this.value == data.card.currentTarget && event.type == 'mouseover') || (this.value == data.card.currentTarget && event.type == 'mousedown')) {
      let g = null;
      if(this.value != '1') {
        g = new createjs.Graphics().beginStroke("#000000").beginFill("#CDCDCD").dc(5.8, 10, sizeScale*1.2);
        this.prev.line.graphics.beginStroke("#000000").lineTo(event.target.parent.x, event.target.parent.y);
        data.card.stage.addChild(this.prev.line);
      }
      else {
        g = new createjs.Graphics().beginStroke("#000000").beginFill("#CDCDCD").dc(5.8, 10, sizeScale*1.2);
      }
      event.target.graphics = g;
      data.card.currentTarget = this.nextTarget;
    }
    else if (this.nextTarget == data.card.currentTarget && event.type == 'mouseout') {
      startPoint = new createjs.Shape();
      startPoint.x = event.target.parent.x;
      startPoint.y = event.target.parent.y;
      this.line = startPoint;
    }
    else if (this.value == data.card.currentTarget && event.type == 'mouseout') {
      if (this.nextTarget == '-1') {
        data.card.completed = true;
      }
      this.prev.line.graphics.lineTo(this.circle.x, this.circle.y);
      let g = new createjs.Graphics().beginStroke("#000000").beginFill("#ffffff").dc(5.8, 10, sizeScale*1.2);
      event.target.graphics = g;
    } else if (this.value != data.card.currentTarget && event.type == 'mouseover') {
      madeMistake = true;
      this.prev.circle.graphics.append(createjs.Graphics.beginCmd);
      let stroke = new createjs.Graphics.Stroke("#ff1744");
      let line = new createjs.Graphics.LineTo(this.circle.x, this.circle.y);
      this.prev.circle.graphics.append(stroke);
      this.prev.circle.graphics.append(line);
      let g = new createjs.Graphics().beginStroke("#000000").beginFill("#ffffff").dc(5.8, 10, sizeScale*1.2);
      event.target.graphics = g;
    }
  }
  event.target.stage.update();
}

function handleClicking(event) {
  ismousedown = event.type == "mousedown" || event.type == "click" ? true : false;
}

class Point {
  constructor(x, y, value, next, prev) {
    this.x = x;
    this.y = y;
    this.value = value;
    this.nextTarget = next;
    this.prev = prev;
    this.selected = null;
    this.line = null;
    // get the size of the canvas with respect to the window.
    this.circle = new createjs.Shape();
  }
}

class Card {
  constructor(stage, card_name) {
    let points = cards[card_name].points;
    this.width = cards[card_name].width;;
    this.height = cards[card_name].height;
    
    var ctx = $('#demoCanvas')[0].getContext('2d'); 
    this.windowWidthScale = ctx.canvas.width / this.width;
    this.windowHeightScale = ctx.canvas.height / this.height;
    this.completed = false;
    this.background = null;
    this.points = [];
    this.selected_points = [];
    this.card_name = card_name;
    this.stage = stage;
    this.next = null;
    this.timer = new Timer();
    this.stage.on("stagemousedown", handleClicking, this, false, null, true);
    this.stage.on("stagemouseup", handleClicking, this, false, null, true);
    if (points !== null) {
      for (let i in points) {
        let point = points[i];
        let newPoint = null;
        if (i == 0) {
          newPoint = new Point(point.x, point.y, point.value, point.next, null);
        } else {
          newPoint = new Point(point.x, point.y, point.value, point.next, this.points[i-1]);
        }
        this.points.push(newPoint);
      }
    }
    this.currentTarget = "1";
  }

  selectPoint(point) {
    point.selected = this.timer.getTimeValues().toString(['hours', 'minutes', 'seconds', 'secondTenths']);
    this.selected_points.push({
      'point': point
    });
    if (point.next == -1 && point.value == 8) {
      this.stop();
    }
  }

  draw() {
    this.shape = new createjs.Shape();
    this.shape.name = "background";
    this.shape.graphics.beginStroke("#000000").beginFill("#ffffff").dr(0, 0, this.width * this.windowWidthScale * 0.6, this.height * this.windowHeightScale * 0.6);
    let containers = [];
    this.stage.enableMouseOver(10);
    for (let point of this.points) {
      let container = new createjs.Container();
      let text = new createjs.Text(point.value, "20px Arial", "#000000");
      let circle = point.circle;
      let sizeScale = Math.max(this.windowWidthScale, this.windowHeightScale);
      circle.graphics.beginStroke("#000000").beginFill("#ffffff").dc(5.8, 10, sizeScale*1.2);
      container.x = point.x * this.windowWidthScale;
      container.y = point.y * this.windowHeightScale;
      circle.on("mouseover", handlePointInteraction, point, false, {card: this}, true);
      circle.on("mouseout", handlePointInteraction, point, false, {card: this}, true);
      circle.on("mousedown", handlePointInteraction, point, false, {card: this}, true);
      circle.on("mouseup", handlePointInteraction, point, false, {card: this}, true);
      container.addChild(circle, text);
      containers.push(container);
    }
    let card_container = new createjs.Container();
    card_container.addChild(this.shape);
    for (let container of containers) {
      card_container.addChild(container);
    }
    card_container.x = this.width*this.windowWidthScale/5;
    card_container.y = this.height * this.windowHeightScale/5;
    this.stage.addChild(card_container);
    this.start();
  }

  start() {
    this.timer.start({
      precision: 'secondTenths'
    });
  }

  stop() {
    this.timer.stop();
  }
}

function beginTest(stage) {
  var card = new Card(stage, 'sample');
  // console.log("starting trial #" + trial_num);
  card.draw(stage);
  stage.update();
}

function init() {
  var stage = new createjs.Stage("demoCanvas");
  createjs.Touch.enable(stage);
  var ctx = $('#demoCanvas')[0].getContext('2d'); 
    var windowWidthScale = ctx.canvas.width / 50;
    var windowHeightScale = ctx.canvas.height / 50;
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
  label.x = 150 / 2;
  label.y = 60 / 2;
  // creating button
  var button = new createjs.Container();
  button.name = "button";
  button.x = 23.1 * windowWidthScale;
  button.y = 16 * windowHeightScale;
  button.addChild(background, label);

  button.addEventListener("click", function (event) {
    let path = window.location.pathname;
    let test_code = path.split('/')[3];
    let url = '/tmt/test-start/' + test_code + '/';
    let csrftoken = $('#demoCanvas input').val();
    let data = stringify({"status": "Started"}, null, 2);
    $.ajax({
      type: "POST",
      url: url,
      headers: {'X-CSRFToken': csrftoken},
      dataType: 'json',
      data: data,
      success: function (data, textStatus, jqXHR) {
        console.log("test has begin");
      },
      fail: function (error) {
        console.log(error);
    }
    });
    stage.removeAllChildren();
    beginTest(stage);
    // beginTrial(stage, 'sample');
  });
  // adding button to stage.
  stage.addChild(instructions_main, instructions_sub, button);
*/
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
/*
  stage.update();
}
*/