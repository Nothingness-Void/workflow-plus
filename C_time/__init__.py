# Initialize the C_time module
from C_time.blocks import TimeBlock
from framework.workflow.core.plugin import Plugin

class CTimePlugin(Plugin):
    def __init__(self, block_registry: BlockRegistry, container: DependencyContainer):
        super().__init__()
        self.block_registry = block_registry
        self.container = container

    def on_load(self):
        logger.info("CTimePlugin loading")

        # 注册TimeBlock
        try:
            self.block_registry.register("time_block", "C_time", TimeBlock)
        except Exception as e:
            logger.warning(f"CTimePlugin failed: {e}")

        # 注册示例工作流
        try:
            with importlib.resources.path('C_time', '__init__.py') as p:
                package_path = p.parent
                example_dir = package_path / 'example'

                if not example_dir.exists():
                    raise FileNotFoundError(f"Example directory not found at {example_dir}")

                yaml_files = list(example_dir.glob('*.yaml')) + list(example_dir.glob('*.yml'))

                for yaml in yaml_files:
                    logger.info(yaml)
                    self.workflow_registry.register("chat", yaml.stem, WorkflowBuilder.load_from_yaml(os.path.join(example_dir, yaml), self.container))
        except Exception as e:
            logger.warning(f"workflow_registry failed: {e}")

    def on_start(self):
        logger.info("CTimePlugin started")

    def on_stop(self):
        logger.info("CTimePlugin stopped")
