import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "coco-2017",
    split="validation",
    classes=["person", "car"],
    label_types=["detections", "segmentations"],
    max_samples=100,
)

if __name__ == "__main__":
    session = fo.launch_app(dataset)
    session.wait()
