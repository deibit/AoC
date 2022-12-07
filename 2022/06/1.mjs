import { readFile } from "node:fs/promises";

async function entry() {
  const contents = await readFile("input", { encoding: "utf8" });
  return Array.from(contents);
}

try {
  const content = await entry();
  for (let idx = 0; idx < content.length; idx++) {
    let sl = content.slice(idx, idx + 4);
    const s = new Set(sl);
    if (s.size === 4) {
      console.log(idx + 4);
      break;
    }
  }
} catch (err) {
  console.error(err.message);
}
