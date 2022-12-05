import { readFile } from "node:fs/promises";
try {
  const contents = await readFile("input", { encoding: "utf8" });
  let elfs = Array();
  let idx = 0;
  let sum = 0;
  const l = contents.split("\n");
  l.map((e) => {
    if (e.length > 0) {
      sum += Number.parseInt(e);
    } else {
      elfs[idx] = sum;
      idx++;
      sum = 0;
    }
  });
  elfs = elfs.sort((a, b) => {
    if (a > b) return -1;
    if (b > a) return 1;
    return 0;
  });
  console.log(elfs.slice(0, 3).reduce((a, c) => a + c, 0));
} catch (err) {
  console.error(err.message);
}
