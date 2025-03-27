import logging

import aiohttp

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def generate_resume(filename):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://resumake.cybar.dev/resume/",
            data={"resume": open(f"{filename}.yaml", "rb")},
        ) as res:
            if res.status == 200:
                pdf_content = await res.read()  # Read response content as bytes
                with open(f"{filename}.pdf", "wb") as pdf_file:
                    pdf_file.write(pdf_content)
            else:
                logger.error(f"Failed to generate resume. Error {res.status}")
