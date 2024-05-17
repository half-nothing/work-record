import path from "path";
import alias from "module-alias";

alias(path.resolve(__dirname, "../"));

import {initCatcher} from "@/base/catcher";
import express from "express";
import type {Request, Response} from "express";
import cookieParser from "cookie-parser";
import session from "express-session";
import {connectionLogger, logger} from "@/base/logger";
import {commonMiddleWare} from "@/middleware/commonMiddleWare";
import {apiRouter} from "@/router/api";
import {Config} from "@/base/config";
import serverConfig = Config.serverConfig;
import process from "node:process";
import https from "https";
import fs from "fs";
import http from "http";
import {FileUtils} from "@/utils/fileUtils";
import checkFileExist = FileUtils.checkFileExist;

// GEC init
initCatcher();
// Create express app
const app = express();

// Allow proxy server like nginx
app.set('trust proxy', true);

// Add middleware
app.use(connectionLogger);
app.use(commonMiddleWare.accessRecord);
app.use(express.urlencoded({extended: false}));
app.use(express.json());
app.use(cookieParser(serverConfig.cookie.key))
app.use(session({
    secret: serverConfig.cookie.key,
    resave: false,
    saveUninitialized: true,
    name: "id",
    cookie: {
        maxAge: serverConfig.cookie.timeout
    },
    rolling: true
}))

// Add router
app.use("/api", apiRouter);

// Matches unmatched requests
app.use('*', (_: Request, res: Response) => {
    logger.info(`Not router match, redirect to home page ${serverConfig.homePage}`);
    res.redirect(serverConfig.homePage);
});

// Add error middleware
app.use(commonMiddleWare.errorHandler)

const port = serverConfig.port;

if (serverConfig.https.enable) {
    if (!checkFileExist(serverConfig.https.keyPath)) {
        logger.error("Can not find certificate key.");
        process.exit(-1);
    }
    if (!checkFileExist(serverConfig.https.crtPath)) {
        logger.error("Can not find certificate crt.");
        process.exit(-1);
    }
    https.createServer({
        key: fs.readFileSync(serverConfig.https.keyPath),
        cert: fs.readFileSync(serverConfig.https.crtPath)
    }, app).listen(port);
    logger.info(`Server running at https://0.0.0.0${port === 443 ? "" : ":" + port}/`);
} else {
    http.createServer(app).listen(port);
    if (serverConfig.https.enableHSTS) {
        logger.error(`If you want to enable HSTS, please enable HTTPS first`);
        process.exit(-1)
    }
    logger.info(`Server running at http://0.0.0.0${port === 80 ? "" : ":" + port}/`);
}