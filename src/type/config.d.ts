type ServerConfig = {
    https: {
        enable: boolean,
        enableHSTS: boolean,
        keyPath: string,
        crtPath: string
    },
    cookie: {
        key: string,
        timeout: number
    },
    callLimit: {
        count: number,
        time: number
    },
    homePage: string,
    port: number
}
