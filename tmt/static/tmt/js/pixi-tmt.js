var windowWidth = window.innerWidth;
var windowHeight = window.innerHeight;

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

let app = new PIXI.Application({
  width: windowWidth, // default: 800
  height: windowHeight, // default: 600
  antialias: true, // default: false
  transparent: false, // default: false 
  resolution: 1 // default: 1
});

app.stage.position.set(windowWidth/2 - 900/2, windowHeight/2 - 500/2);

let outlinedStage = new PIXI.Graphics();
outlinedStage.beginFill(0xFBFBFB);
outlinedStage.lineStyle(3, 0x000000);
outlinedStage.drawRect(0, 0, 880, 480);
outlinedStage.endFill();
app.stage.addChild(outlinedStage);

var madeMistake = false;
var isMousePressed = false;

class Point {
    constructor(x, y, value, next, prev) {
        this.x = x;
        this.y = y;
        this.value = value;
        this.nextTarget = next;
        this.prev = prev;
        this.selected = null;
        this.line = null;

        let container = new PIXI.Container();
        let circle = new PIXI.Graphics();
        circle.beginFill(0x9966FF);
        circle.drawCircle(0, 0, 25);
        circle.endFill();
        circle.zOrder = 2;
        container.x = x * 9;
        container.y = y * 9;

        let message = new PIXI.Text(value);
        message.position.set(-7.45, -15);
        message.zOrder = 3;
        container.interactive = true;
        container.addChild(circle);
        container.addChild(message);
        container.zOrder = 2;
        this.circle = container;
    }
  }
  
  class Card {
    constructor(app, card_name) {
      let points = cards[card_name].points;
      this.width = cards[card_name].width;
      this.height = cards[card_name].height;

      this.completed = false;
      this.background = null;
      this.points = [];
      this.lines = [];
      this.selected_points = [];
      this.card_name = card_name;
      this.app = app;
      this.timer = new Timer();
      if (points !== null) {
        for (let i in points) {
          let point = points[i];
          let newPoint = null;
          if (i == 0) {
            newPoint = new Point(point.x, point.y, point.value, point.next, null);
          } else {
            newPoint = new Point(point.x, point.y, point.value, point.next, this.points[i-1]);
          }
          newPoint.circle.card = this;
          newPoint.circle.on('mouseover', this.enteredEventHandler);
          newPoint.circle.on('mouseout', this.exitedEventHandler);
          newPoint.circle.on('mousedown', this.mousePressedEvent);
          newPoint.circle.on('mouseup', this.mousePressedEvent);
          this.points.push(newPoint);
        }
        this.currentTarget = this.points[0];
      }
    }

    draw() {
        for (let point of this.points) {
            app.stage.addChild(point.circle);
        }
    }

    exitedEventHandler(event) {
        event.currentTarget.off('mouseover', this.enteredEventHandler);
        event.currentTarget.off('mouseout', this.exitedEventHandler);
    }

    enteredEventHandler(event) {
        card = event.currentTarget.card;
        if (isMousePressed && !madeMistake) {
            if (event.currentTarget.children[1].text === card.currentTarget.value) {
                if (card.currentTarget.value === card.points[0].value) {
                    let xVal = event.currentTarget.x;
                    let yVal = event.currentTarget.y;
                    let newLine = new PIXI.Graphics();
                    newLine.moveTo(xVal, yVal);
                    newLine.lineStyle(5, 0x000000, 1, 0.5);
                    newLine.zOrder = 1;
                    card.lines.push(newLine);
                    card.currentTarget = card.points[parseInt(card.currentTarget.nextTarget)-1];

                    let circle = event.currentTarget.children[0];
                    circle.clear();
                    circle.beginFill(0x4fc3f7);
                    circle.drawCircle(0, 0, 25);
                    circle.endFill();
                }
                else if (card.currentTarget.nextTarget === "-1") {
                    let xVal = event.currentTarget.x;
                    let yVal = event.currentTarget.y;
                    card.completed = true;
                    let currentLine = card.lines[card.points.indexOf(card.currentTarget)-1];
                    app.stage.addChildAt(currentLine, 1);
                    currentLine.lineTo(xVal, yVal);
                    let message = new PIXI.Text("Finished Card!", {fontFamily : 'Arial', fontSize: 24, fill : 0xff1010, align : 'center'});
                    message.position.set(card.app.stage.width/2, card.app.stage.height/2);
                    card.app.stage.addChild(message);
                }
                else {
                    let xVal = event.currentTarget.x;
                    let yVal = event.currentTarget.y;
                    let newLine = new PIXI.Graphics();
                    newLine.moveTo(xVal, yVal);
                    newLine.lineStyle(5, 0x000000, 1, 0.5);
                    newLine.zOrder = 1;
                    card.lines.push(newLine);
                    let currentLine = card.lines[card.points.indexOf(card.currentTarget)-1];
                    app.stage.addChildAt(currentLine, 1);
                    currentLine.lineTo(xVal, yVal);
                    card.currentTarget = card.points[parseInt(card.currentTarget.nextTarget)-1];
                }
            }
            else {
                let xVal = event.currentTarget.x;
                let yVal = event.currentTarget.y;
                let currentLine = card.lines[card.points.indexOf(card.currentTarget)-1];
                currentLine.lineStyle(5, 0xff0000, 1, 0.5);
                card.app.stage.addChildAt(currentLine, 1);
                currentLine.lineTo(xVal, yVal);
                madeMistake = true;
                
                let circle = event.currentTarget.children[0];
                circle.clear();
                circle.beginFill(0xff5252);
                circle.drawCircle(0, 0, 25);
                circle.endFill();
            }
        } 
        else if(isMousePressed && madeMistake) {
            if (event.currentTarget.children[1].text === card.currentTarget.value) {
                if (card.currentTarget.value === card.points[0].value) {
                    let xVal = event.currentTarget.children[1].x;
                    let yVal = event.currentTarget.children[1].y;
                    let newLine = new PIXI.Graphics();
                    newLine.position.set(xVal, yVal);
                    newLine.lineStyle(5, 0x000000, 1, 0.5);
                    newLine.zOrder = 1;
                    card.lines.push(newLine);
                    card.currentTarget = card.points[parseInt(card.currentTarget.nextTarget)-1];
                }
                else if (card.currentTarget.nextTarget === "-1") {
                    card.completed = true;
                    let message = new PIXI.Text("Finished Card!", {fontFamily : 'Arial', fontSize: 24, fill : 0xff1010, align : 'center'});
                    message.moveTo(card.app.stage.width/2, card.app.stage.height/2);
                    card.app.stage.addChild(message);
                }
                else {
                    let xVal = event.currentTarget.x;
                    let yVal = event.currentTarget.y;
                    let newLine = new PIXI.Graphics();
                    newLine.moveTo(xVal, yVal);
                    newLine.lineStyle(5, 0x000000, 1, 0.5);
                    card.lines.pop();
                    card.lines.push(newLine);
                    let currentLine = card.lines[card.points.indexOf(card.currentTarget)-1];
                    currentLine.zOrder = 1;
                    card.app.stage.addChildAt(currentLine, 1);
                    currentLine.lineTo(xVal, yVal);
                    card.currentTarget = card.points[parseInt(card.currentTarget.nextTarget)-1]
                }
            }
        }
        console.log("entered");
    }

    mousePressedEvent(event) {
        isMousePressed = event.type == 'mousedown' ? true : false;
        if (event.currentTarget.children[1].text === card.currentTarget.value) {
            if (card.currentTarget.value === card.points[0].value) {
                let xVal = event.currentTarget.x;
                let yVal = event.currentTarget.y;
                let newLine = new PIXI.Graphics();
                newLine.moveTo(xVal, yVal);
                newLine.lineStyle(5, 0x000000, 1, 0.5);
                newLine.zOrder = 1;
                card.lines.push(newLine);
                card.currentTarget = card.points[parseInt(card.currentTarget.nextTarget)-1];
            }
        }
        console.log("mouse is pressed: " + isMousePressed);
    }
    
}

app.renderer.backgroundColor = 0xfbfbfb;
document.body.appendChild(app.view);

app.renderer.autoResize = true;

let card = new Card(app, 'sample');

card.draw();
