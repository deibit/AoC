import { assert } from "node:console";
import { readFile } from "node:fs/promises";

async function entry() {
  const contents = await readFile("input", { encoding: "utf8" });
  return contents.split("\n");
}

function explore_tree(root, level, sizes) {
  if (root.size <= 100000) sizes.push(root.size);
  console.log(`${"   ".repeat(level)}${root.name}: (size: ${root.size})`);
  root.dirs.map((e) => explore_tree(e, level + 1, sizes));
  root.files.map((e) => console.log(`${"   ".repeat(level)} ${e}`));
  return sizes;
}

function get_all_dirs(root, dirs) {
  dirs.push(root);
  root.dirs.map((e) => get_all_dirs(e, dirs));
  return dirs;
}

function propagate_size_up(node, size) {
  if (node === undefined) return;
  node.size += size;
  propagate_size_up(node.parent, size);
}

try {
  const commands = await entry();
  let root = { parent: undefined, dirs: [], files: [], size: 0, name: "/" };
  let current = root;

  for (let index = 1; index < commands.length; index++) {
    const command = commands[index];

    switch (command[0]) {
      case "$": {
        // is a cd [dir] or ls
        let lcommand = command.split(" ");
        if (lcommand.length === 2) continue;
        let dir = lcommand[2];
        switch (dir) {
          case "..": {
            // cd ..
            assert(current.parent !== "undefined");
            current = current.parent;
            break;
          }
          default: {
            // cd [dir]
            current = current.dirs.find((e) => e.name === dir);
            assert(current !== "undefined");
          }
        }
        break;
      }

      default: {
        // is a entry from a 'ls'
        const entry = command.split(" ");
        switch (entry[0]) {
          case "dir": {
            // is a dir
            if (!current.dirs.includes(entry[1])) {
              current.dirs.push({
                parent: current,
                dirs: [],
                files: [],
                size: 0,
                name: entry[1],
              });
            }
            break;
          }
          default: {
            // is a file
            if (!current.files.includes(entry[1])) {
              current.files.push(`${entry[1]} ${entry[0]}`);
              propagate_size_up(current, parseInt(entry[0]));
            }
          }
        }
      }
    }
  }
  const free = 70000000 - root.size;
  const target = 30000000 - free;
  console.log(`needed ${target} of space`);
  const dirs = get_all_dirs(root, new Array());
  let selected = dirs[0];
  for (let index = 1; index < dirs.length; index++) {
    const element = dirs[index];
    if (element.size - target < 0) {
      continue;
    }
    if (element.size - target < selected.size - target) {
      selected = element;
    }
  }
  console.log(`found dir with size: ${selected.size}`);
} catch (err) {
  console.error(err.message);
}
