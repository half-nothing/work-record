import {logger} from "@/base/logger";
import {Utils} from "@/utils/utils";
import {Request, Response, NextFunction} from "express";

export namespace commonMiddleWare {
    import enableHSTS = Utils.enableHSTS;
    export const accessRecord = (req: Request, res: Response, next: NextFunction) => {
        enableHSTS(res);
        logger.info(`[${req.protocol}] Client request ${req.path} from ${req.ip}`);
        next();
    }
    export const errorHandler = (err: Error, _: Request, res: Response, __: NextFunction) => {
        logger.error(`Server Error! ${err.message}`);
        res.status(500);
        res.send("Server Error!")
    }
}