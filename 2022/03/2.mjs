import { readFile } from "node:fs/promises";

function score(letter) {
  const value = letter.charCodeAt();
  if (letter.toUpperCase() == letter) {
    return value - 38;
  }
  return value - 96;
}

try {
  const contents = await readFile("input", { encoding: "utf8" });
  let lines = contents.split("\n");
  let total = 0;
  for (let index = 0; index < lines.length; index += 3) {
    let [a, b, c] = lines
      .slice(index, index + 3)
      .map((e) => Array.from(new Set(e)));

    let todos = a.concat(b).concat(c).sort();

    for (let idx = 0; idx < todos.length; idx++) {
      if (todos[idx] === todos[idx + 1]) {
        if (todos[idx] === todos[idx + 2]) {
          total += score(todos[idx]);
          break;
        }
      }
    }
  }
  console.log(total);
} catch (err) {
  console.error(err.message);
}
