#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\n24614664:\n > ")
API_HASH = input("\na45d425fa87925ac8f7567dd5fdd6c2e:\n > ")

i = c("yukkistring", in_memory=True, api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nBQF3lwgAmi8BNh7fa3YiphaA09bvVhPgCHSR7fRKtwh2Y93s8iFGnk1J60Ma8Emx4A37htbX9PwXLX4PX4Q_f0J9IiqfIQqa-_CWrKPTkhmjWpTDnbjaY0AkJ-jN3mcrmXjH2p4-2zzRsAuzJ32e1WXnMGhtfSfGfgXIzd94nt1MS9jnOXqEykHneSQPAB-bcyFr6baw6tA0Zldpu-KZKOwljEMe7g9G4uepBuHJ-gMDg2UCigMo7zmuBrCPZnMyIxBSEc6iuuhaAFPI6eHD7RDnGsoOrvJ3eDFpQST908tV6PlCt_YZbr2mDl6srUT-J9mBgCn37z4sHMGPKHRQC_8W7hJ1VAAAAAHHyClrAA,/ COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
    print("\n STRING GENERATED\n")
    xx = f"BQF3lwgAmi8BNh7fa3YiphaA09bvVhPgCHSR7fRKtwh2Y93s8iFGnk1J60Ma8Emx4A37htbX9PwXLX4PX4Q_f0J9IiqfIQqa-_CWrKPTkhmjWpTDnbjaY0AkJ-jN3mcrmXjH2p4-2zzRsAuzJ32e1WXnMGhtfSfGfgXIzd94nt1MS9jnOXqEykHneSQPAB-bcyFr6baw6tA0Zldpu-KZKOwljEMe7g9G4uepBuHJ-gMDg2UCigMo7zmuBrCPZnMyIxBSEc6iuuhaAFPI6eHD7RDnGsoOrvJ3eDFpQST908tV6PlCt_YZbr2mDl6srUT-J9mBgCn37z4sHMGPKHRQC_8W7hJ1VAAAAAHHyClrAA, COPY IT, DON'T SHARE!!\n\n`{ss}`\n\n STRING GENERATED"
    try:
        await i.send_message("me", xx)
    except BaseException:
        pass


asyncio.run(main())
