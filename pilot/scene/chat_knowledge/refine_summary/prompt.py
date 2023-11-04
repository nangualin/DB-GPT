from pilot.prompts.prompt_new import PromptTemplate
from pilot.configs.config import Config
from pilot.scene.base import ChatScene
from pilot.common.schema import SeparatorStyle

from pilot.scene.chat_knowledge.refine_summary.out_parser import (
    ExtractRefineSummaryParser,
)

CFG = Config()


PROMPT_SCENE_DEFINE = """"""

_DEFAULT_TEMPLATE_ZH = """根据提供的上下文信息，我们已经提供了一个到某一点的现有总结:{existing_answer}\n 请再完善一下原来的总结。\n回答的时候最好按照1.2.3.点进行总结"""

_DEFAULT_TEMPLATE_EN = """
We have provided an existing summary up to a certain point: {existing_answer}\nWe have the opportunity to refine the existing summary (only if needed) with some more context below.please refine the original summary. 
\nWhen answering, it is best to summarize according to points 1.2.3.
"""

_DEFAULT_TEMPLATE = (
    _DEFAULT_TEMPLATE_EN if CFG.LANGUAGE == "en" else _DEFAULT_TEMPLATE_ZH
)

PROMPT_RESPONSE = """"""

PROMPT_SEP = SeparatorStyle.SINGLE.value

PROMPT_NEED_NEED_STREAM_OUT = False

prompt = PromptTemplate(
    template_scene=ChatScene.ExtractRefineSummary.value(),
    input_variables=["existing_answer"],
    response_format="",
    template_define=PROMPT_SCENE_DEFINE,
    template=_DEFAULT_TEMPLATE + PROMPT_RESPONSE,
    stream_out=PROMPT_NEED_NEED_STREAM_OUT,
    output_parser=ExtractRefineSummaryParser(
        sep=PROMPT_SEP, is_stream_out=PROMPT_NEED_NEED_STREAM_OUT
    ),
)

CFG.prompt_template_registry.register(prompt, is_default=True)
