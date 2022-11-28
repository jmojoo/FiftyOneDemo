import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "voc-2007",
    split="validation",
    classes=["person", "car"],
    max_samples=100,
)

if __name__ == "__main__":
    session = fo.launch_app(dataset)
    session.wait()
