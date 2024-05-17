/**
 * @class
 * @name Tracker
 * @description API访问限制器类
 * @author Half_nothing
 * @version 1.0.2
 * @since 1.0.0
 * @export
 */
export class Tracker {
    private readonly limit: number;
    private readonly windowSize: number;
    private ipWindows: Map<string, { start: number, count: number }>;

    /**
     * @function
     * @public
     * @desc 构造函数
     * @param limit {number} API访问限制
     * @param windowSize {number} 滑动窗口大小
     * @version 1.0.0
     * @since 1.3.0
     * @export
     */
    constructor(limit: number, windowSize: number) {
        this.limit = limit;
        this.windowSize = windowSize;
        this.ipWindows = new Map();
    }

    /**
     * @function
     * @public
     * @desc 检查ip是否超出访问限制
     * @param ip {string} 客户端ip
     * @return {true} 没有超出限制
     * @return {false} 超出访问限制
     * @version 1.0.0
     * @since 1.0.0
     * @export
     */
    trackIP(ip: string): boolean {
        const now = Date.now();
        if (this.ipWindows.has(ip)) {
            const window = this.ipWindows.get(ip)!;
            if (now - window.start >= this.windowSize) {
                window.start = now;
                window.count = 1;
                return window.count <= this.limit;
            }
            window.count++;
            return window.count <= this.limit;
        }
        const window = {start: now, count: 1};
        this.ipWindows.set(ip, window);
        return true;
    }
}
