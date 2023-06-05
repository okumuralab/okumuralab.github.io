const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
const scale = 20;
const rows = canvas.height / scale;
const columns = canvas.width / scale;

const tetriminoShapes = [
  [
    [1, 1, 1],
    [0, 1, 0],
  ],
  [
    [0, 1, 1],
    [1, 1, 0],
  ],
  [
    [1, 1, 0],
    [0, 1, 1],
  ],
  [
    [1, 1],
    [1, 1],
  ],
  [
    [1, 1, 1, 1],
  ],
  [
    [1, 1, 1],
    [1, 0, 0],
  ],
  [
    [1, 1, 1],
    [0, 0, 1],
  ],
];

class Piece {
  constructor() {
    this.shape = this.randomShape();
    this.position = { x: Math.floor(columns / 2) - 1, y: 0 };
  }

  randomShape() {
    const shape = tetriminoShapes[Math.floor(Math.random() * tetriminoShapes.length)];
    return JSON.parse(JSON.stringify(shape));
  }

  draw() {
    ctx.fillStyle = 'lime';
    for (let y = 0; y < this.shape.length; y++) {
      for (let x = 0; x < this.shape[y].length; x++) {
        if (this.shape[y][x]) {
          ctx.fillRect((this.position.x + x) * scale, (this.position.y + y) * scale, scale, scale);
          ctx.strokeStyle = 'black';
          ctx.strokeRect((this.position.x + x) * scale, (this.position.y + y) * scale, scale, scale);
        }
      }
    }
  }

  moveDown() {
    this.position.y++;
  }

  moveLeft() {
    this.position.x--;
  }

  moveRight() {
    this.position.x++;
  }

  rotate() {
    const temp = JSON.parse(JSON.stringify(this.shape));
    for (let y = 0; y < this.shape.length; ++y) {
      for (let x = 0; x < this.shape[y].length; ++x) {
        this.shape[y][x] = temp[this.shape[y].length - x - 1][y];
      }
    }
  }
}

class Board {
  constructor() {
    this.matrix = this.createMatrix(columns, rows);
  }

  createMatrix(w, h) {
    const matrix = [];
    while (h--) {
      matrix.push(new Array(w).fill(0));
    }
    return matrix;
  }

  draw() {
    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < columns; x++) {
        if (this.matrix[y][x]) {
          ctx.fillStyle = 'cyan';
          ctx.fillRect(x * scale, y * scale, scale, scale);
          ctx.strokeStyle = 'black';
          ctx.strokeRect(x * scale, y * scale, scale, scale);
        }
      }
    }
  }

  collide(piece) {
    const shape = piece.shape;
    const position = piece.position;
    for (let y = 0; y < shape.length; y++) {
      for (let x = 0; x < shape[y].length; x++) {
        if (shape[y][x] &&
          (this.matrix[y + position.y] && this.matrix[y + position.y][x + position.x]) !== 0) {
          return true;
        }
      }
    }
    return false;
  }

  merge(piece) {
    for (let y = 0; y < piece.shape.length; y++) {
      for (let x = 0; x < piece.shape[y].length; x++) {
        if (piece.shape[y][x]) {
          this.matrix[y + piece.position.y][x + piece.position.x] = 1;
        }
      }
    }
  }

  clearLines() {
    outer: for (let y = rows - 1; y >= 0; y--) {
      for (let x = 0; x < columns; x++) {
        if (!this.matrix[y][x]) {
          continue outer;
        }
      }

      this.matrix.splice(y, 1);
      this.matrix.unshift(new Array(columns).fill(0));
    }
  }

  clear() {
    ctx.fillStyle = '#222';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }
}

// Game variables and instances
const board = new Board();
let piece = new Piece();
let dropCounter = 0;
let dropInterval = 1000;
let lastTime = 0;

// Update the game state
function update(time = 0) {
  const deltaTime = time - lastTime;
  lastTime = time;

  dropCounter += deltaTime;
  if (dropCounter > dropInterval) {
    if (board.collide(piece)) {
      board.merge(piece);
      board.clearLines();
      piece = new Piece();
      if (board.collide(piece)) {
        // Game over
        board.matrix = board.createMatrix(columns, rows);
      }
    } else {
      piece.moveDown();
    }
    dropCounter = 0;
  }

  board.clear();
  board.draw();
  piece.draw();
  requestAnimationFrame(update);
}

// Move the piece only if it's not colliding
Piece.prototype.moveDown = function () {
  this.position.y++;
  if (board.collide(this)) {
    this.position.y--;
    board.merge(this);
    board.clearLines();
    this.reset();
  }
};

Piece.prototype.moveLeft = function () {
  this.position.x--;
  if (board.collide(this)) {
    this.position.x++;
  }
};

Piece.prototype.moveRight = function () {
  this.position.x++;
  if (board.collide(this)) {
    this.position.x--;
  }
};

Piece.prototype.rotate = function () {
  const temp = JSON.parse(JSON.stringify(this.shape));
  const rows = this.shape.length;
  const cols = this.shape[0].length;
  let newShape = new Array(cols).fill().map(() => new Array(rows).fill(0));

  for (let y = 0; y < rows; ++y) {
    for (let x = 0; x < cols; ++x) {
      newShape[x][rows - 1 - y] = temp[y][x];
    }
  }

  const offset = this.position.x <= 0 ? 1 : -1;
  if (board.collide({ shape: newShape, position: this.position })) {
    if (!board.collide({ shape: newShape, position: { x: this.position.x + offset, y: this.position.y } })) {
      this.position.x += offset;
    } else {
      return;
    }
  }

  this.shape = newShape;
};

Piece.prototype.reset = function () {
  this.shape = this.randomShape();
  this.position = { x: Math.floor(columns / 2) - 1, y: 0 };

  if (board.collide(this)) {
    // Game over
    board.matrix = board.createMatrix(columns, rows);
  }
};

function handleKeyPress(event) {
  if (event.keyCode === 37) {
    piece.moveLeft();
  } else if (event.keyCode === 39) {
    piece.moveRight();
  } else if (event.keyCode === 40) {
    piece.moveDown();
  } else if (event.keyCode === 38) {
    piece.rotate();
  }
}

document.addEventListener('keydown', handleKeyPress);
update();
