import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "cifar-10",
)

if __name__ == "__main__":
    session = fo.launch_app(dataset)
    session.wait()
