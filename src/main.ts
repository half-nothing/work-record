import path from "path";
import alias from "module-alias";

alias(path.resolve(__dirname, "../"));

console.log("Hello World")