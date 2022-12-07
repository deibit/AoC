import { readFile } from "node:fs/promises";

try {
  const contents = await readFile("input", { encoding: "utf8" });
  let lines = contents.split("\n");
  let overlaps = 0;
  for (let idx = 0; idx < lines.length; idx++) {
    let [a, b] = lines[idx].split(",");
    let [aa, ab] = a.split("-").map((e) => parseInt(e));
    let [ba, bb] = b.split("-").map((e) => parseInt(e));

    if (ab < ba || aa > bb) continue;
    overlaps++;
  }
  console.log(overlaps);
} catch (err) {
  console.error(err.message);
}
