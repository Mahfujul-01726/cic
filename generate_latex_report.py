# -*- coding: utf-8 -*-
"""
LaTeX Report Generator for Chemical Image Classification
Converts the Word report's text, tables, code, and figures into a professional LaTeX document.
"""

import os

# Define relative paths from the workspace root for LaTeX compiling
# (We use forward slashes which are compatible with LaTeX on Windows and Linux)
latex_file_path = "Chemical_Image_Classification_Report.tex"

content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage[table]{xcolor}
\usepackage{float}
\usepackage{listings}
\usepackage{amsmath}
\usepackage{tabularx}
\usepackage{subcaption}
\usepackage{grffile} % Helps LaTeX handle spaces in filenames
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage[most]{tcolorbox}
\usepackage{lmodern}
\usepackage{helvet}
\usepackage{microtype}

% --- Color Palette Definitions ---
\definecolor{deepblue}{RGB}{0, 70, 127}
\definecolor{slateepblue}{RGB}{31, 78, 121}
\definecolor{lightgray}{RGB}{240, 240, 240}
\definecolor{darkgreen}{RGB}{0, 100, 0}
\definecolor{charcoal}{RGB}{30, 30, 30}

% --- Page Header/Footer Configuration ---
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\color{charcoal}\small\sffamily Chemical Image Classification Research Report}
\fancyhead[R]{\color{charcoal}\small\sffamily July 2026}
\fancyfoot[C]{\color{charcoal}\small\sffamily Page \thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\headheight}{14pt}

% --- Section Title Formatting ---
\titleformat{\section}{\color{deepblue}\normalfont\Large\bfseries\sffamily}{\thesection}{1em}{}[{\color{deepblue}\titlerule[0.8pt]}]
\titleformat{\subsection}{\color{slateepblue}\normalfont\large\bfseries\sffamily}{\thesubsection}{1em}{}
\titleformat{\subsubsection}{\color{charcoal}\normalfont\normalsize\bfseries\sffamily}{\thesubsubsection}{1em}{}

% --- Syntax Highlighting Configuration for Listings ---
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    backgroundcolor=\color{lightgray!30},
    keywordstyle=\color{blue}\bfseries,
    stringstyle=\color{purple},
    commentstyle=\color{darkgreen}\itshape,
    showstringspaces=false,
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    numbersep=8pt,
    frame=leftline,
    framerule=2.5pt,
    rulecolor=\color{deepblue},
    framexleftmargin=5pt,
    xleftmargin=15pt,
    breaklines=true,
    breakatwhitespace=true,
    tabsize=4
}

\hypersetup{
    colorlinks=true,
    linkcolor=deepblue,
    urlcolor=deepblue,
    citecolor=deepblue
}

\begin{document}
\pagenumbering{gobble}

% ==============================================================================
% COVER PAGE
% ==============================================================================
\begin{titlepage}
    \thispagestyle{empty}
    \centering
    \vspace*{1.5cm}
    {\Huge\bfseries\color{deepblue} LABORATORY REPORT\par}
    \vspace{0.4cm}
    {\color{slateepblue}\hrule height 2pt}
    \vspace{0.8cm}
    {\Large\bfseries\color{slateepblue} Chemical Image Classification\par}
    \vspace{0.3cm}
    {\large\itshape A Full Deep Learning Research Pipeline\par}
    \vspace{1.5cm}
    
    \begin{figure}[H]
        \centering
        \includegraphics[width=0.6\textwidth]{chemical_classification_models/samples and distrubutation/raw dataset/train_samples.png}
    \end{figure}
    \vspace{1cm}
    
    \renewcommand{\arraystretch}{1.4}
    \begin{tabularx}{\textwidth}{>{\bfseries\color{deepblue}}l X}
        \toprule
        Task & Chemical Image Classification using Deep Learning \\
        Platform & Google Colab (T4 GPU) + TensorFlow 2.20.0 \\
        Dataset & Patent Chemical Images — 4 Classes, 16,000 Images \\
        Models & VGG16, DenseNet121, ResNet50V2, InceptionV3, MobileNetV2, Xception, EfficientNetB4, ConvNeXtTiny, Custom CNN \\
        Date & July 2026 \\
        \bottomrule
    \end{tabularx}
    
    \vfill
\end{titlepage}

% ==============================================================================
% TABLE OF CONTENTS
% ==============================================================================
\newpage
\pagenumbering{roman}
\thispagestyle{plain}
\tableofcontents
\newpage
\pagenumbering{arabic}

% ==============================================================================
% SECTION 1: INTRODUCTION
% ==============================================================================
\section{Introduction \& Task Requirements}
This report documents a complete deep learning research pipeline for classifying chemical images extracted from scientific publications and patent documents. The dataset contains four distinct categories of chemical imagery, and the objective was to design, train, and evaluate multiple deep learning architectures — both pre-trained transfer learning models and a custom-built CNN.

\subsection{Assigned and Performed Tasks}
\begin{itemize}
    \item Show sample images from every class.
    \item Show class-wise image quantity across train/validation/test sets using a bar plot.
    \item Perform image preprocessing and data augmentation.
    \item Use pre-trained models: VGG16, DenseNet121, ResNet50V2, InceptionV3, MobileNetV2, Xception, EfficientNetB4, and ConvNeXtTiny — with architectural modifications.
    \item Build and train a Custom CNN; ensemble models if required.
    \item Show model summaries.
    \item Plot accuracy and loss curves for training and validation sets.
    \item Compute Accuracy, Precision, Recall, F1-Score, Confusion Matrix, AUC, and ROC Curves.
    \item Generate Grad-CAM heatmaps to visualise model attention regions.
    \item Generate LIME explanations for model predictions.
\end{itemize}

% ==============================================================================
% SECTION 2: DATASET OVERVIEW
% ==============================================================================
\section{Dataset Overview \& Directory Structure}
The dataset consists of chemical images sourced from patent documents and scientific journals. Images were standardised to PNG format before training. The dataset is split into three sets: Training, Validation, and Test — with perfectly balanced class distribution.

\subsection{Class Descriptions}
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\textwidth}{>{\bfseries\color{deepblue}}l X}
    \toprule
    Class Name & Description \\
    \midrule
    one\_molecule & Images containing a single molecular structure or compound diagram. \\
    reactions & Images depicting chemical reactions with reagents, arrows, and products. \\
    rest & Other chemical-related images not fitting the above categories. \\
    several\_molecules & Images containing multiple molecular structures arranged together. \\
    \bottomrule
\end{tabularx}
\caption{Class Descriptions}
\label{tab:class_desc}
\end{table}

\subsection{Dataset Split Summary}
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabular}{l c c c c c}
    \toprule
    \textbf{Split} & \textbf{one\_molecule} & \textbf{reactions} & \textbf{rest} & \textbf{several\_molecules} & \textbf{Total} \\
    \midrule
    Train & 3,200 & 3,200 & 3,200 & 3,200 & 12,800 \\
    Validation & 400 & 400 & 400 & 400 & 1,600 \\
    Test & 400 & 400 & 400 & 400 & 1,600 \\
    \midrule
    \textbf{Grand Total} & \textbf{4,000} & \textbf{4,000} & \textbf{4,000} & \textbf{4,000} & \textbf{16,000} \\
    \bottomrule
\end{tabular}
\caption{Dataset Split Summary}
\label{tab:dataset_split}
\end{table}

\subsection{Directory Structure}
\begin{lstlisting}[language=sh,numbers=none]
dataset_png/
  |-- train/
  |     |-- one_molecule/      (3,200 images)
  |     |-- reactions/         (3,200 images)
  |     |-- rest/              (3,200 images)
  |     `-- several_molecules/ (3,200 images)
  |-- validation/
  |     `-- [400 images per class]
  `-- test/
        `-- [400 images per class]
\end{lstlisting}

% ==============================================================================
% SECTION 3: SAMPLE IMAGES
% ==============================================================================
\section{Sample Images from Every Class}
Random sample images were displayed from each of the four classes across all three dataset splits. A grid of 4 samples per class was generated for each split using matplotlib.

\begin{lstlisting}[language=Python]
SAMPLES_PER_CLASS = 4
fig, axes = plt.subplots(NUM_CLASSES, SAMPLES_PER_CLASS, figsize=(16, 16))
fig.suptitle('Training Set Samples', fontsize=22, fontweight='bold')
for row, cls in enumerate(CLASSES):
    cls_dir = os.path.join(TRAIN_DIR, cls)
    imgs    = get_images(cls_dir)
    chosen  = random.sample(imgs, min(SAMPLES_PER_CLASS, len(imgs)))
    for col, path in enumerate(chosen):
        ax.imshow(load_image_rgb(path))
plt.tight_layout() ; plt.show()
\end{lstlisting}

\subsection{Raw Training Set Samples}
4 randomly selected images from each class in the training split:
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/samples and distrubutation/raw dataset/train_samples.png}
    \caption{Raw Training Set — 4 samples $\times$ 4 classes}
    \label{fig:train_samples_raw}
\end{figure}

\subsection{Raw Validation Set Samples}
4 randomly selected images from each class in the validation split:
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/samples and distrubutation/raw dataset/validation_samples.png}
    \caption{Raw Validation Set — 4 samples $\times$ 4 classes}
    \label{fig:val_samples_raw}
\end{figure}

\subsection{Raw Test Set Samples}
4 randomly selected images from each class in the test split:
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/samples and distrubutation/raw dataset/test_samples.png}
    \caption{Raw Test Set — 4 samples $\times$ 4 classes}
    \label{fig:test_samples_raw}
\end{figure}

% ==============================================================================
% SECTION 4: BAR PLOT
% ==============================================================================
\section{Class-wise Image Distribution (Bar Plot)}
A grouped bar chart was produced showing the number of images per class across all three splits. The dataset is perfectly balanced — every class has equal counts in each split, ensuring unbiased model training.

\begin{lstlisting}[language=Python]
x = np.arange(len(CLASSES))  ;  width = 0.25
splits = ['train','validation','test']
colors = ['#2196F3','#4CAF50','#FF9800']
for idx, (split, color) in enumerate(zip(splits, colors)):
    values = [counts[split][cls] for cls in CLASSES]
    ax.bar(x + idx*width, values, width, label=split.capitalize(), color=color)
ax.set_title('Class-wise Image Distribution Across Splits')
plt.savefig('step2_class_distribution.png', dpi=150)
\end{lstlisting}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{chemical_classification_models/samples and distrubutation/raw dataset/class_distribution.png}
    \caption{Class-wise Image Distribution Across Train / Validation / Test Splits}
    \label{fig:class_dist}
\end{figure}

% ==============================================================================
% SECTION 5: PREPROCESSING & DATA AUGMENTATION
% ==============================================================================
\section{Image Preprocessing \& Augmentation}
All images were standardised and augmented using Keras \texttt{ImageDataGenerator}. The following pipeline was applied to the training set:

\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabularx}{\textwidth}{>{\bfseries\color{deepblue}}l X}
    \toprule
    Augmentation Parameter & Value / Setting \\
    \midrule
    Rescaling & 1/255 — normalise pixel values to [0, 1] \\
    Rotation Range & $\pm$20$^{\circ}$ \\
    Width Shift Range & 15\% of image width \\
    Height Shift Range & 15\% of image height \\
    Shear Range & 10\% \\
    Zoom Range & 20\% \\
    Horizontal Flip & Enabled \\
    Vertical Flip & Enabled \\
    Fill Mode & Nearest \\
    Validation Split & 20\% of training images \\
    \bottomrule
\end{tabularx}
\caption{Image Augmentation Parameters}
\label{tab:augmentation}
\end{table}

\begin{lstlisting}[language=Python]
train_datagen = ImageDataGenerator(
    rescale=1./255, rotation_range=20,
    width_shift_range=0.15, height_shift_range=0.15,
    shear_range=0.1, zoom_range=0.2,
    horizontal_flip=True, vertical_flip=True,
    validation_split=0.2, fill_mode='nearest'
)
# Generators
train_gen = ...flow_from_directory(..., subset='training')   # 10,240 images
val_gen   = ...flow_from_directory(..., subset='validation') #  2,560 images
test_gen  = val_test_datagen.flow_from_directory(...)        #  1,600 images
\end{lstlisting}

\subsection{Preprocessed Class Distribution}
After preprocessing, the class balance is maintained across all splits. The bar chart below shows the image counts per class after augmentation-ready PNG conversion:
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{chemical_classification_models/samples and distrubutation/preprocess dataset/Figure_Preprocessed_Class_Distribution.png}
    \caption{Preprocessed Dataset — Class Distribution (Train / Val / Test)}
    \label{fig:class_dist_prep}
\end{figure}

\subsection{Preprocessed Training Set Samples}
Sample images from the training set after preprocessing (resized, normalised):
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/samples and distrubutation/preprocess dataset/train_preprocessed_samples.png}
    \caption{Preprocessed Training Set Samples — 4 samples $\times$ 4 classes}
    \label{fig:train_samples_prep}
\end{figure}

\subsection{Preprocessed Validation Set Samples}
Sample images from the validation set after preprocessing:
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/samples and distrubutation/preprocess dataset/validation_preprocessed_samples.png}
    \caption{Preprocessed Validation Set Samples — 4 samples $\times$ 4 classes}
    \label{fig:val_samples_prep}
\end{figure}

\subsection{Preprocessed Test Set Samples}
Sample images from the test set after preprocessing:
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/samples and distrubutation/preprocess dataset/test_preprocessed_samples.png}
    \caption{Preprocessed Test Set Samples — 4 samples $\times$ 4 classes}
    \label{fig:test_samples_prep}
\end{figure}

% ==============================================================================
% SECTION 6: MODEL ARCHITECTURE
% ==============================================================================
\section{Model Architecture \& Design}

\subsection{Transfer Learning Framework}
A unified function \texttt{build\_transfer\_model()} applies the same classification head to every pre-trained base model:
\begin{itemize}
    \item Pre-trained base (ImageNet weights, \texttt{include\_top=False})
    \item Global Average Pooling 2D
    \item Batch Normalization
    \item Dense(512, ReLU) + Dropout(0.5)
    \item Dense(256, ReLU) + Dropout(0.25)
    \item Dense(4, Softmax) — output layer
\end{itemize}

\begin{lstlisting}[language=Python]
def build_transfer_model(base_model_fn, input_shape=(224,224,3),
                         num_classes=4, dropout=0.5, fine_tune_from=None):
    base = base_model_fn(weights='imagenet', include_top=False,
                         input_shape=input_shape)
    base.trainable = False
    inputs = Input(shape=input_shape)
    x = base(inputs, training=False)
    x = GlobalAveragePooling2D()(x)
    x = BatchNormalization()(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.25)(x)
    outputs = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs, outputs)
    # Selective fine-tuning of last N layers
    model.compile(optimizer=Adam(1e-4),
                  loss='categorical_crossentropy', metrics=['accuracy'])
    return model
\end{lstlisting}

\subsection{Pre-trained Models Used}
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabularx}{\textwidth}{>{\bfseries}l l l X}
    \toprule
    Model & Input Size & Epochs / Fine-tune & Key Characteristic \\
    \midrule
    VGG16 & 224$\times$224 & 5 / fine\_tune\_from=8 & Oxford VGG 16-layer deep CNN \\
    DenseNet121 & 224$\times$224 & 5 / fine\_tune\_from=20 & Dense skip connections between all layers \\
    ResNet50V2 & 224$\times$224 & 5 / fine\_tune\_from=20 & Improved residual learning (V2) \\
    InceptionV3 & 299$\times$299 & 3 / fine\_tune\_from=20 & Multi-scale inception modules \\
    MobileNetV2 & 224$\times$224 & 3 / fine\_tune\_from=30 & Lightweight depthwise separable convs \\
    Xception & 299$\times$299 & 5 / fine\_tune\_from=20 & Extreme inception — full depthwise convs \\
    EfficientNetB4 & 224$\times$224 & 5 / fine\_tune\_from=30 & Compound width/depth/resolution scaling \\
    ConvNeXtTiny & 224$\times$224 & 5 / fine\_tune\_from=20 & Modern pure ConvNet, ViT-inspired design \\
    \bottomrule
\end{tabularx}
\caption{Pre-trained Models Configuration}
\label{tab:pretrained_models_desc}
\end{table}

\subsection{Custom CNN Architecture}
A deep custom CNN was built with 4 convolutional blocks + a classification head:
\begin{lstlisting}[language=Python]
def build_custom_cnn(input_shape=(224,224,3), num_classes=4):
    # Block 1:  Conv2D(64) x 2  + BN + MaxPool + Dropout(0.20)
    # Block 2:  Conv2D(128) x 2 + BN + MaxPool + Dropout(0.25)
    # Block 3:  Conv2D(256) x 2 + BN + MaxPool + Dropout(0.30)
    # Block 4:  Conv2D(512) x 2 + BN + MaxPool + Dropout(0.35)
    # Head:     GlobalAvgPool -> Dense(512)+BN+Drop(0.5)
    #           -> Dense(256)+Drop(0.3) -> Dense(4, softmax)
    model.compile(optimizer=Adam(1e-3), loss='categorical_crossentropy')
\end{lstlisting}

% ==============================================================================
% SECTION 7: TRAINING CONFIG
% ==============================================================================
\section{Training Configuration \& Callbacks}
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabularx}{\textwidth}{>{\bfseries\color{deepblue}}l X}
    \toprule
    Parameter & Value \\
    \midrule
    Optimizer & Adam (lr = $10^{-4}$) \\
    Loss Function & Categorical Cross-Entropy \\
    Batch Size & 32 \\
    Epochs per Model & 3 – 5 (with Early Stopping) \\
    Image Size (most) & 224$\times$224 px \\
    Image Size (Inception/Xception) & 299$\times$299 px \\
    TensorFlow Version & 2.20.0 \\
    Hardware & Google Colab T4 GPU \\
    Random Seed & 42 \\
    \bottomrule
\end{tabularx}
\caption{Training Parameters}
\label{tab:training_params}
\end{table}

\subsection{Callbacks Used}
\begin{itemize}
    \item \textbf{EarlyStopping}: patience=7, monitor=val\_accuracy, restore\_best\_weights=True.
    \item \textbf{ReduceLROnPlateau}: factor=0.3, patience=3, min\_lr=1e-7, monitor=val\_loss.
    \item \textbf{ModelCheckpoint}: saves best model as .keras file to Google Drive.
\end{itemize}

% ==============================================================================
% SECTION 8: MODEL SUMMARIES
% ==============================================================================
\section{Model Summaries}
Detailed model summaries were generated using \texttt{model.summary()} and saved as text files. The summaries show every layer, its output shape, and the total trainable and non-trainable parameter counts. The table below shows the approximate parameter counts for each model:

\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabularx}{\textwidth}{>{\bfseries}l l X}
    \toprule
    Model & Base Params (approx.) & Notes \\
    \midrule
    VGG16 & 138 M & Heaviest model, no skip connections \\
    DenseNet121 & 7 M & Parameter-efficient due to dense connections \\
    ResNet50V2 & 25 M & Residual blocks reduce vanishing gradients \\
    InceptionV3 & 23 M & Multi-scale feature extraction \\
    MobileNetV2 & 3.4 M & Lightest model, designed for mobile \\
    Xception & 22 M & Depthwise separable convolutions \\
    EfficientNetB4 & 19 M & Compound scaling \\
    ConvNeXtTiny & 28 M & Latest architecture, ViT-inspired \\
    Custom CNN & $\sim$10 M & 4-block from-scratch CNN \\
    \bottomrule
\end{tabularx}
\caption{Model Parameters Summary}
\label{tab:param_summary}
\end{table}

% ==============================================================================
% SECTION 9: ACCURACY & LOSS CURVES
% ==============================================================================
\section{Accuracy \& Loss Curves}
For each trained model, combined accuracy and loss curves are plotted showing both training and validation performance across epochs. These curves help diagnose overfitting or underfitting behaviour.

\begin{lstlisting}[language=Python]
for name, history in histories.items():
    plt.subplot(1,2,1)
    plt.plot(history['accuracy'],     label='Train')
    plt.plot(history['val_accuracy'], label='Validation')
    plt.subplot(1,2,2)
    plt.plot(history['loss'],     label='Train')
    plt.plot(history['val_loss'], label='Validation')
\end{lstlisting}

\subsection{Performance Curves Grid}
The figures below show the accuracy and loss history for each architecture.

\begin{figure}[H]
\centering
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/VGG16.png}
  \caption{VGG16}
  \label{fig:curve_vgg}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/DenseNet121.png}
  \caption{DenseNet121}
  \label{fig:curve_dense}
\end{subfigure}

\vspace{0.5cm}

\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/ResNet50V2.png}
  \caption{ResNet50V2}
  \label{fig:curve_resnet}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/InceptionV3.png}
  \caption{InceptionV3}
  \label{fig:curve_inception}
\end{subfigure}
\caption{Training and Validation Accuracy/Loss Curves (VGG16, DenseNet121, ResNet50V2, InceptionV3)}
\label{fig:accuracy_loss_curves_g1}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/MobileNetV2.png}
  \caption{MobileNetV2}
  \label{fig:curve_mobile}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/Xception.png}
  \caption{Xception}
  \label{fig:curve_xception}
\end{subfigure}

\vspace{0.5cm}

\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/EfficientNetB4.png}
  \caption{EfficientNetB4}
  \label{fig:curve_effnet}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/ConvNeXtTiny.png}
  \caption{ConvNeXtTiny}
  \label{fig:curve_convnext}
\end{subfigure}
\caption{Training and Validation Accuracy/Loss Curves (MobileNetV2, Xception, EfficientNetB4, ConvNeXtTiny)}
\label{fig:accuracy_loss_curves_g2}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.65\textwidth]{chemical_classification_models/Accuracy_Loss_Curves/CustomCNN.png}
\caption{Training and Validation Accuracy/Loss Curves (Custom CNN)}
\label{fig:curve_custom}
\end{figure}

% ==============================================================================
% SECTION 10: MODEL PERFORMANCE METRICS
% ==============================================================================
\section{Model Performance Metrics}
All 9 models were evaluated on the held-out test set (1,600 images). Metrics computed: Accuracy, Precision (weighted), Recall (weighted), F1-Score (weighted).

\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabular}{l c c c c}
    \toprule
    \textbf{Model} & \textbf{Accuracy} & \textbf{Precision} & \textbf{Recall} & \textbf{F1-Score} \\
    \midrule
    \rowcolor{green!10} \textbf{VGG16} & \textbf{0.9106} & \textbf{0.9115} & \textbf{0.9106} & \textbf{0.9104} \\
    ResNet50V2 & 0.8988 & 0.8990 & 0.8988 & 0.8985 \\
    DenseNet121 & 0.8913 & 0.8912 & 0.8913 & 0.8910 \\
    InceptionV3 & 0.8863 & 0.8901 & 0.8863 & 0.8866 \\
    Xception & 0.8088 & 0.8093 & 0.8088 & 0.8089 \\
    ConvNeXtTiny & 0.7688 & 0.8152 & 0.7688 & 0.7763 \\
    MobileNetV2 & 0.7688 & 0.8338 & 0.7688 & 0.7552 \\
    EfficientNetB4 & 0.3938 & 0.5850 & 0.3938 & 0.3227 \\
    CustomCNN & 0.2694 & 0.3267 & 0.2694 & 0.1504 \\
    \bottomrule
\end{tabular}
\caption{Model Performance Evaluation on Test Set}
\label{tab:perf_metrics}
\end{table}

\begin{tcolorbox}[colback=deepblue!5!white,colframe=deepblue!75!black,title=Performance Evaluation Summary,arc=2pt,left=8pt,right=8pt]
\textbf{Best Model Highlight}: \textbf{VGG16} achieved the highest accuracy (\textbf{91.06\%}) and F1-Score (\textbf{91.04\%}). EfficientNetB4 and CustomCNN underperformed — EfficientNet likely due to preprocessing incompatibility (built-in normalisation conflicting with the rescale=1./255 pipeline), and CustomCNN due to insufficient training data for a from-scratch model.
\end{tcolorbox}

% ==============================================================================
% SECTION 11: CONFUSION MATRIX
% ==============================================================================
\section{Confusion Matrix \& Classification Report}
Seaborn heatmap confusion matrices were generated for all 9 models. Each cell shows the number of test images predicted as a given class for each true class.

\subsection{VGG16 Classification Report (Best Model)}
\begin{lstlisting}[numbers=none,backgroundcolor=\color{lightgray!50}]
                   precision    recall  f1-score   support

     one_molecule       0.89      0.94      0.92       400
        reactions       0.94      0.86      0.90       400
             rest       0.93      0.94      0.94       400
several_molecules       0.89      0.89      0.89       400

          accuracy                           0.91      1600
         macro avg       0.91      0.91      0.91      1600
      weighted avg       0.91      0.91      0.91      1600
\end{lstlisting}

\subsection{Confusion Matrices Grid}
\begin{figure}[H]
\centering
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/VGG16_Confusion_Matrix.png}
  \caption{VGG16}
  \label{fig:cm_vgg}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/DenseNet121_Confusion_Matrix.png}
  \caption{DenseNet121}
  \label{fig:cm_dense}
\end{subfigure}

\vspace{0.5cm}

\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/ResNet50V2_Confusion_Matrix.png}
  \caption{ResNet50V2}
  \label{fig:cm_resnet}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/InceptionV3_Confusion_Matrix.png}
  \caption{InceptionV3}
  \label{fig:cm_inception}
\end{subfigure}
\caption{Confusion Heatmaps (VGG16, DenseNet121, ResNet50V2, InceptionV3)}
\label{fig:confusion_matrices_g1}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/MobileNetV2_Confusion_Matrix.png}
  \caption{MobileNetV2}
  \label{fig:cm_mobile}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/Xception_Confusion_Matrix.png}
  \caption{Xception}
  \label{fig:cm_xception}
\end{subfigure}

\vspace{0.5cm}

\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/EfficientNetB4_Confusion_Matrix.png}
  \caption{EfficientNetB4}
  \label{fig:cm_effnet}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Confusion_Matrix/ConvNeXtTiny_Confusion_Matrix.png}
  \caption{ConvNeXtTiny}
  \label{fig:cm_convnext}
\end{subfigure}
\caption{Confusion Heatmaps (MobileNetV2, Xception, EfficientNetB4, ConvNeXtTiny)}
\label{fig:confusion_matrices_g2}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.65\textwidth]{chemical_classification_models/Confusion_Matrix/CustomCNN_Confusion_Matrix.png}
\caption{Confusion Heatmap (Custom CNN)}
\label{fig:cm_custom}
\end{figure}

% ==============================================================================
% SECTION 12: ROC CURVES
% ==============================================================================
\section{ROC Curve \& AUC}
Multi-class ROC curves were computed using the One-vs-Rest (OvR) strategy with label binarization. The AUC (Area Under the Curve) was macro-averaged across all 4 classes.

\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabular}{l c}
    \toprule
    \textbf{Model} & \textbf{AUC (Macro-Avg)} \\
    \midrule
    \rowcolor{green!10} \textbf{VGG16} & \textbf{0.9890} \\
    InceptionV3 & 0.9846 \\
    DenseNet121 & 0.9832 \\
    ResNet50V2 & 0.9821 \\
    MobileNetV2 & 0.9614 \\
    Xception & 0.9554 \\
    ConvNeXtTiny & 0.9459 \\
    EfficientNetB4 & 0.7105 \\
    CustomCNN & 0.6743 \\
    \bottomrule
\end{tabular}
\caption{ROC Area Under the Curve (AUC) Summary}
\label{tab:auc_metrics}
\end{table}

\subsection{ROC Curves Grid}
\begin{figure}[H]
\centering
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/VGG16_ROC.png}
  \caption{VGG16}
  \label{fig:roc_vgg}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/DenseNet121_ROC.png}
  \caption{DenseNet121}
  \label{fig:roc_dense}
\end{subfigure}

\vspace{0.5cm}

\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/ResNet50V2_ROC.png}
  \caption{ResNet50V2}
  \label{fig:roc_resnet}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/InceptionV3_ROC.png}
  \caption{InceptionV3}
  \label{fig:roc_inception}
\end{subfigure}
\caption{One-vs-Rest (OvR) ROC Curves (VGG16, DenseNet121, ResNet50V2, InceptionV3)}
\label{fig:roc_curves_g1}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/MobileNetV2_ROC.png}
  \caption{MobileNetV2}
  \label{fig:roc_mobile}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/Xception_ROC.png}
  \caption{Xception}
  \label{fig:roc_xception}
\end{subfigure}

\vspace{0.5cm}

\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/EfficientNetB4_ROC.png}
  \caption{EfficientNetB4}
  \label{fig:roc_effnet}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth]{chemical_classification_models/Results/ROC_Curves/ConvNeXtTiny_ROC.png}
  \caption{ConvNeXtTiny}
  \label{fig:roc_convnext}
\end{subfigure}
\caption{One-vs-Rest (OvR) ROC Curves (MobileNetV2, Xception, EfficientNetB4, ConvNeXtTiny)}
\label{fig:roc_curves_g2}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.65\textwidth]{chemical_classification_models/Results/ROC_Curves/CustomCNN_ROC.png}
\caption{One-vs-Rest (OvR) ROC Curve (Custom CNN)}
\label{fig:roc_custom}
\end{figure}

% ==============================================================================
% SECTION 13: GRAD-CAM
% ==============================================================================
\section{Grad-CAM Visualisation}
Gradient-weighted Class Activation Mapping (Grad-CAM) was applied to VGG16 (using the \texttt{block5\_conv3} convolutional layer) to visualise which image regions the model focused on during classification.

\subsection{How Grad-CAM Works}
Grad-CAM computes the gradient of the predicted class score with respect to the last convolutional layer's feature maps. These gradients are global-average-pooled to produce class-discriminative weights, which are combined with the feature maps to create a heatmap. The heatmap is overlaid on the original image using a jet colour map.

\begin{lstlisting}[language=Python]
grad_model = tf.keras.models.Model(
    inputs=[base_model.input],
    outputs=[base_model.get_layer('block5_conv3').output, base_model.output]
)
with tf.GradientTape() as tape:
    conv_outputs, predictions = grad_model(img_tensor)
    class_channel = tf.gather(predictions[0], pred_index)
grads       = tape.gradient(class_channel, conv_outputs)
pooled_grads = tf.reduce_mean(grads, axis=(0,1,2))
heatmap     = conv_outputs[0] @ pooled_grads[..., tf.newaxis]
heatmap     = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
\end{lstlisting}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/Results/Visualizations/GradCAM_VGG16_Fixed.png}
    \caption{Grad-CAM Heatmaps — VGG16 (one row per class, original + overlay)}
    \label{fig:gradcam}
\end{figure}

% ==============================================================================
% SECTION 14: LIME EXPLAINABILITY
% ==============================================================================
\section{LIME Explainability}
LIME (Local Interpretable Model-agnostic Explanations) was applied to the VGG16 model. LIME perturbs the input image into superpixel segments and fits a local linear model around each prediction to identify which image regions support or contradict the prediction.

\subsection{Output per class (3 subplot columns)}
\begin{itemize}
    \item \textbf{Original Image} — raw test image from the class.
    \item \textbf{Positive Regions (Green)} — superpixels that supported the top predicted class.
    \item \textbf{Negative Regions (Red)} — superpixels that worked against the top prediction.
\end{itemize}

\begin{lstlisting}[language=Python]
explainer = lime_image.LimeImageExplainer()
explanation = explainer.explain_instance(
    img_array.astype('double'),
    predict_fn,      # model.predict wrapper
    top_labels=4, hide_color=0, num_samples=1000
)
temp, mask = explanation.get_image_and_mask(
    top_label, positive_only=True, hide_rest=False
)
\end{lstlisting}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{chemical_classification_models/Results/Visualizations/LIME_VGG16_Explanations.png}
    \caption{LIME Explanations — VGG16 (all 4 classes)}
    \label{fig:lime}
\end{figure}

% ==============================================================================
% SECTION 15: CONCLUSION
% ==============================================================================
\section{Conclusion \& Key Findings}
This report presents a comprehensive deep learning pipeline for chemical image classification. Nine different architectures were trained and evaluated:

\begin{itemize}
    \item \textbf{VGG16} achieved the best overall performance (Accuracy: 91.06\%, AUC: 0.9890), making it the most suitable model for this task.
    \item \textbf{ResNet50V2} and \textbf{DenseNet121} also performed strongly ($\sim$89–90\% accuracy), confirming that residual and dense connection architectures transfer well to chemical imagery.
    \item \textbf{InceptionV3} (88.6\%, AUC: 0.9846) and \textbf{Xception} (80.9\%) showed competitive results using 299$\times$299 input.
    \item \textbf{MobileNetV2} and \textbf{ConvNeXtTiny} both achieved 76.9\% accuracy; MobileNetV2 suits deployment where model size is constrained.
    \item \textbf{EfficientNetB4} underperformed significantly (39.4\%) — likely due to its built-in normalization conflicting with the rescale=1./255 generator pipeline.
    \item The \textbf{Custom CNN} achieved only 26.9\% accuracy, showing that training a deep CNN from scratch on 12,800 images is insufficient without pre-trained features.
    \item \textbf{Grad-CAM} confirmed VGG16 correctly focused on molecular bonds, reaction arrows, and structural patterns — validating genuine feature learning.
    \item \textbf{LIME explanations} showed clear positive (green) regions aligned with key chemical structures, providing interpretable evidence for each prediction.
\end{itemize}

\subsection{Final Model Ranking by Accuracy}
\begin{table}[H]
\centering
\renewcommand{\arraystretch}{1.2}
\rowcolors{2}{lightgray!15}{white}
\begin{tabular}{llcc}
    \toprule
    \textbf{Rank} & \textbf{Model} & \textbf{Accuracy} & \textbf{AUC} \\
    \midrule
    \rowcolor{green!10} \textbf{1st} & \textbf{VGG16} & \textbf{91.06\%} & \textbf{0.9890} \\
    2nd & ResNet50V2 & 89.88\% & 0.9821 \\
    3rd & DenseNet121 & 89.13\% & 0.9832 \\
    4th & InceptionV3 & 88.63\% & 0.9846 \\
    5th & Xception & 80.88\% & 0.9554 \\
    6th & MobileNetV2 & 76.88\% & 0.9614 \\
    6th & ConvNeXtTiny & 76.88\% & 0.9459 \\
    8th & EfficientNetB4 & 39.38\% & 0.7105 \\
    9th & Custom CNN & 26.94\% & 0.6743 \\
    \bottomrule
\end{tabular}
\caption{Final Model Ranking by Accuracy and AUC}
\label{tab:final_ranking_summary}
\end{table}

\vspace{2em}
\begin{center}
    \itshape\color{gray} — End of Report —
\end{center}

\end{document}
"""

with open(latex_file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated {latex_file_path} successfully!")
