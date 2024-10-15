# Age and Gender Detection Using Masked Faces

This project is research-based, where we attempt to guess the **age** and **gender** of individuals using their facial features, even when part of their faces is covered with a mask.

You can find the project repository [here](https://github.com/Vishnu30603/Age-and-Gender-Detection-).

## Datasets Used

### 1. UTK-Face
We utilized the **UTKFace** dataset, which offers a diverse range of facial images with varying demographics. We modified this dataset to include masked versions of the faces.
- You can learn more about how we masked the faces [here](https://github.com/aqeelanwar/MaskTheFace).

### 2. FGNET-Masked
The **FGNET** dataset was also used. A masked version of this dataset is available on Kaggle.
- You can access the FGNET-masked dataset [here](https://www.kaggle.com/datasets/vatsapatel09/fgnet-mask-dataset).

### 3. Our Custom Dataset
We collected our own pictures of locals to create a custom dataset and trained the model on this dataset as well.
![Sample Image](images/Custom Dataset.png)

## Goal

The main objective of this research is to identify the **age** and **gender** of a person with minimal facial features (due to mask-wearing). We trained the model on multiple datasets to ensure diverse results and to make accurate future predictions.

## Dataset Preprocessing

The following preprocessing steps were performed:
- Images were converted to grayscale.
- Images were resized to **48x48** pixels for uniformity.
- All processed images were stored in a CSV file for easy manipulation and processing.

## Training

The model was trained using **30 epochs** and produced the following results:

- **Age Accuracy**: 91%
- **Gender Accuracy**: 98%

## Testing

On testing the model, the results were:

- **Age Accuracy**: 46%
- **Gender Accuracy**: 88%

## What I Learned

This project provided valuable insights into:
1. **Dataset Preparation**: Collecting images, processing them according to specific needs, and preprocessing existing datasets.
2. **Model Training**: Training the model to achieve desired results for both age and gender prediction.
3. **Testing**: Evaluating the model's performance on test data to identify areas of improvement.

## References

- [MaskTheFace GitHub Repository](https://github.com/aqeelanwar/MaskTheFace)
- [FGNET-Mask Dataset on Kaggle](https://www.kaggle.com/datasets/vatsapatel09/fgnet-mask-dataset)
