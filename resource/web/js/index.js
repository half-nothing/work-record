const durationChart = echarts.init(document.getElementById('durationContainer'), 'light', {renderer: 'canvas'});
const durationOption = {
    tooltip: {
        formatter: '{a} <br/>{b} : {c}h'
    },
    series: [
        {
            name: '兼职时长',
            type: 'gauge',
            startAngle: 200,
            endAngle: -20,
            min: 0,
            max: 100,
            progress: {
                show: true
            },
            detail: {
                valueAnimation: true,
                formatter: '{value}h'
            },
            data: [
                {
                    value: 0,
                    name: '兼职时长'
                }
            ]
        }
    ]
};
durationChart.setOption(durationOption);
const allDurationChart = echarts.init(document.getElementById('allDurationContainer'), 'light', {renderer: 'canvas'});
const allDurationOption = {
    tooltip: {
        trigger: 'axis',
        formatter: function (params) {
            return (
                params[0].axisValue + " : " + params[0].data + "h"
            )
        },
        axisPointer: {
            animation: false
        }
    },
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            data: [150, 230, 224, 218, 135, 147, 260],
            type: 'line'
        }
    ]
};
allDurationChart.setOption(allDurationOption);

function updateDurationTime(time, month, year) {
    durationOption.series[0].data[0] = {
        value: time,
        name: `${year}年${month}月`
    };
    durationChart.setOption(durationOption);
}

function updateAllDurationTime(axis, times) {
    allDurationOption.xAxis.data = axis;
    allDurationOption.series[0].data = times;
    allDurationChart.setOption(allDurationOption);
}