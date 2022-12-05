import { readFile } from "node:fs/promises";

try {
  const rules = {
    A: { X: 3, Y: 4, Z: 8 },
    B: { X: 1, Y: 5, Z: 9 },
    C: { X: 2, Y: 6, Z: 7 },
  };
  let contents = await readFile("input", { encoding: "utf8" });
  let lines = contents.split("\n");
  let acc = 0;
  lines.map((e) => {
    let l, r;
    [l, r] = e.split(" ");
    acc += rules[l][r];
  });
  console.log(acc);
} catch (err) {
  console.error(err.message);
}
