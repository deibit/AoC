import { readFile } from "node:fs/promises";

try {
  let contents = await readFile("input", { encoding: "utf8" });
  let lines = contents.split("\n");
} catch (err) {
  console.error(err.message);
}
