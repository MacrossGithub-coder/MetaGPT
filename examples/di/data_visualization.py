import asyncio

from metagpt.logs import logger
from metagpt.roles.di.data_interpreter import DataInterpreter
from metagpt.utils.recovery_util import save_history


async def main(requirement: str = ""):
    di = DataInterpreter()
    rsp = await di.run(requirement)
    logger.info(rsp)
    save_history(role=di)


if __name__ == "__main__":
    # requirement = "Run data analysis on sklearn Iris dataset, include a plot"
    requirement = "读取当前工作目录d:/Users/Public/macross/MetaGPT/examples/di/nbim-1742264244206.csv文件,并绘制柱状图"
    asyncio.run(main(requirement))