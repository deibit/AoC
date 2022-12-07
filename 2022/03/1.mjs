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
  let l = new Array();
  for (let index = 0; index < lines.length; index++) {
    const element = lines[index];
    let a = Array.from(element.slice(0, element.length / 2));
    let b = Array.from(element.slice(element.length / 2));
    for (let index = 0; index < a.length; index++) {
      const element = a[index];
      if (b.includes(element)) {
        l.push(element);
        break;
      }
    }
  }
  let s = new Array();
  l.map((e) => s.push(score(e)));
  l.map((e) => console.log(e, score(e)));
  console.log(s.reduce((a, c) => a + c, 0));
} catch (err) {
  console.error(err.message);
}
