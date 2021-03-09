from aws_cdk import core
from data_platform.data_lake.stack import DataLakeStack
from data_platform.common_stack import CommonStack
from data_platform.dms.stack import DmsStack

app = core.App()
data_lake = DataLakeStack(app)
common_stack = CommonStack(app)
dms = DmsStack(app, common_stack=common_stack, data_lake_raw_bucket=data_lake.data_lake_raw_bucket)
app.synth()
