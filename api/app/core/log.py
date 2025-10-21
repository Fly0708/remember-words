import sys
from pathlib import Path

from loguru import logger

log_config = {
    "handlers": [
        # Handler 1: 输出到控制台 (Console)
        # 这个 handler 主要用于开发和调试
        {
            "sink": sys.stderr,  # 使用 sys.stderr 来输出
            "level": "INFO",     # 控制台只显示 INFO 及以上级别
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                      "<level>{level: <8}</level> | "
                      "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            "colorize": True,    # 开启颜色
        },

        # Handler 2: 记录所有 INFO 级别以上的日志到文件
        # 按天滚动，例如：logs/all_2025-10-21.log
        {
            "sink":  f"{Path(__file__).parent.parent.parent}" + "/logs/all_{time:YYYY-MM-DD}.log",
            "level": "INFO",
            "rotation": "00:00",     # 每天午夜 (00:00) 创建一个新文件
            "retention": "30 days",   # 日志文件保留7天
            "compression": "zip",    # 使用 zip 压缩旧的日志文件
            "enqueue": True,         # 异步写入，提高性能
            "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        },

        # Handler 3: 单独记录 ERROR 级别以上的日志到文件
        # 按天滚动，例如：logs/error_2025-10-21.log
        {
            "sink": f"{Path(__file__).parent.parent.parent}" + "/logs/error_{time:YYYY-MM-DD}.log",
            "level": "ERROR",        # 只记录 ERROR 及以上级别
            "rotation": "00:00",     # 每天午夜滚动
            "retention": "90 days",  # 错误日志保留30天（通常比普通日志久）
            "compression": "zip",
            "enqueue": True,         # 异步
            "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        },
    ],
    # "extra": {"user_id": "default"} # 可以在这里设置全局的 "extra" 字段
}

# --- 如何使用这个配置 ---

# 1. (重要) 移除 loguru 默认的 handler
logger.remove()

# 2. 加载你的配置
logger.configure(**log_config)

import os
os.makedirs(Path(__file__).parent.parent.parent / "logs", exist_ok=True)