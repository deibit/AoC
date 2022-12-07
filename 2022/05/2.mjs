import { readFile } from "node:fs/promises";

const skip = 10;

async function entry() {
  const contents = await readFile("input", { encoding: "utf8" });
  return contents.split("\n");
}

function get_moves(line) {
  let parts = line.split(" ");
  return { count: parts[1] - 0, from: parts[3] - 1, to: parts[5] - 1 };
}

try {
  const content = await entry();
  let moves = content.slice(skip).map((e) => get_moves(e));
  let stacks = [
    ["S", "L", "W"],
    ["J", "T", "N", "Q"],
    ["S", "C", "H", "F", "J"],
    ["T", "R", "M", "W", "N", "G", "B"],
    ["T", "R", "L", "S", "D", "H", "Q", "B"],
    ["M", "J", "B", "V", "F", "H", "R", "L"],
    ["D", "W", "R", "N", "J", "M"],
    ["B", "Z", "T", "F", "H", "N", "D", "J"],
    ["H", "L", "Q", "N", "B", "F", "T"],
  ];
  moves.map((e) => {
    let tmp_crate = [];
    for (let i = 0; i < e.count; i++) {
      tmp_crate.push(stacks[e.from].pop());
    }
    tmp_crate.reverse();
    tmp_crate.map((elem) => stacks[e.to].push(elem));
  });
  let word = [];
  stacks.map((e) => word.push(e.pop()));
  console.log(word.join(""));
} catch (err) {
  console.error(err.message);
}
