import { readFile } from "node:fs/promises";

// A: Rock, B: Paper, C: Scissors
// X: Rock, Y: Paper, Z: Scissors

const rules = {
  A: { X: 3, Y: 6, Z: 0 },
  B: { X: 0, Y: 3, Z: 6 },
  C: { X: 6, Y: 0, Z: 3 },
};
const values = { X: 1, Y: 2, Z: 3 };
try {
  const contents = await readFile("input", { encoding: "utf8" });
  let lines = contents.split("\n");
  let acc = 0;
  lines.map((e) => {
    let [l, r] = e.split(" ");
    acc += rules[l][r] + values[r];
  });
  console.log(acc);
} catch (err) {
  console.error(err.message);
}
