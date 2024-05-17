import express from "express";
import {apiMiddleWare} from "@/middleware/apiMiddleWare";

export const apiRouter = express.Router();

apiRouter.use(apiMiddleWare.checkCallLimit);