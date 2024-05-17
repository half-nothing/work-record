import {accessSync, constants, writeFileSync, mkdirSync, readdirSync, statSync, WriteFileOptions} from "fs";
import {join} from "path";

/**
 * @namespace FileUtils
 * @desc 文件系统操作类
 * @export
 */
export namespace FileUtils {

    /**
     * @function
     * @desc 检查一个目录是否存在
     * @desc 如果不存在且createFile为true则创建该目录
     * @param path {string} 要检查的目录
     * @param createDir {boolean} 如若目录不存在是否创建目录
     * @param callback {Runnable<boolean>} 回调函数
     * @return {true} 存在
     * @return {false} 不存在
     * @return {void} 当传入回调函数时不返回值
     * @version 1.0.0
     * @since 1.0.0
     * @export
     */
    export function checkDirExist(path: string, createDir: boolean = false, callback?: Runnable<boolean>): void | boolean {
        try {
            accessSync(path, constants.F_OK);
            return callback ? callback(true) : true;
        } catch (_) {
            if (createDir) {
                mkdirSync(path, {recursive: true});
            }
            return callback ? callback(false) : false;
        }
    }

    /**
     * @function
     * @desc 检查一个文件是否存在
     * @desc 如果不存在且createFile为true则创建该文件并写入内容data
     * @desc options为文件写入时候的选项
     * @param path {string} 要检查的文件路径
     * @param createFile {boolean} 如若文件不存在是否创建文件
     * @param data {string} 要写入文件的内容,默认为空文件
     * @param options {WriteFileOptions} 写入文件时的选项,默认为"utf-8"
     * @param callback {Runnable<boolean>} 回调函数
     * @return {true} 存在
     * @return {false} 不存在
     * @return {void} 当传入回调函数时不返回值
     * @version 1.0.0
     * @since 1.0.0
     * @export
     */
    export function checkFileExist(path: string, createFile: boolean = false, data: string = "",
                                   options: WriteFileOptions = 'utf-8', callback?: Runnable<boolean>): void | boolean {
        try {
            accessSync(path, constants.F_OK);
            return callback ? callback(true) : true;
        } catch (_) {
            if (createFile) {
                writeFileSync(path, data, options);
            }
            return callback ? callback(false) : false;
        }
    }
}
