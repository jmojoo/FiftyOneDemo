import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "quickstart",
)

if __name__ == "__main__":
    session = fo.launch_app(dataset)
    session.wait()
