import { assert } from "node:console";
import { readFile } from "node:fs/promises";

async function entry() {
  const contents = await readFile("input", { encoding: "utf8" });
  return contents.split("\n");
}

try {
  const content = await entry();
  const grid = Array();
  for (let index = 0; index < content.length; index++) {
    grid.push(Array.from(content[index]).map((e) => parseInt(e)));
  }

  const maxRow = grid.length - 1;
  const maxCol = grid[0].length - 1;
  let visibles = Array();

  for (let row = 1; row < maxRow; row++) {
    // from left to rigth
    let max = grid[row][0];
    for (let col = 1; col < maxCol; col++) {
      const elem = grid[row][col];
      if (elem > max) {
        if (!visibles.find((e) => e.r === row && e.c === col)) {
          visibles.push({ r: row, c: col });
        }
        max = elem;
      }
    }
    // from right to left
    max = grid[row][maxCol];
    for (let col = maxCol; col > 0; col--) {
      const elem = grid[row][col];
      if (elem > max) {
        if (!visibles.find((e) => e.r === row && e.c === col)) {
          visibles.push({ r: row, c: col });
        }
        max = elem;
      }
    }
  }

  for (let col = 1; col < maxCol; col++) {
    // from top to down
    let max = grid[0][col];
    for (let row = 0; row < maxRow; row++) {
      const elem = grid[row][col];
      if (elem > max) {
        if (!visibles.find((e) => e.r === row && e.c === col)) {
          visibles.push({ r: row, c: col });
        }
        max = elem;
      }
    }
    // from down to top
    max = grid[maxRow][col];
    for (let row = maxRow; row > 0; row--) {
      const elem = grid[row][col];
      if (elem > max) {
        if (!visibles.find((e) => e.r === row && e.c === col)) {
          visibles.push({ r: row, c: col });
        }
        max = elem;
      }
    }
  }

  const edgeVisibleTrees = (maxCol + 1) * 4 - 4;

  console.log(`edges: ${edgeVisibleTrees}`);
  console.log(`trees: ${visibles.length}`);
  console.log(edgeVisibleTrees + visibles.length);
} catch (err) {
  console.error(err.message);
}
