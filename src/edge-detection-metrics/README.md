<!--
 * @Author: Hivan Du
 * @mail: doo@hivan.me
 * @LastEditors: Hivan Du
 * @LastEditTime: 2024-12-13 18:29:47
-->

## 边缘检测指标

探索 RMSE、PSNR、SSIM 和 FOM 对海岸线提取边缘检测的有效性

该存储库包含重现会议论文中结果所需的代码：

C. O'Sullivan, S. Coveney, X. Monteys and S. Dev, "The Effectiveness of Edge Detection Evaluation Metrics for Automated Coastline Detection," 2023 Photonics & Electromagnetics Research Symposium (PIERS), 2023, pp. 31-40, doi: 10.1109/PIERS59004.2023.10221292. [可在此处获得](https://arxiv.org/abs/2405.11498)

本代码仅用于学术和研究目的。如果你打算使用全部或部分代码，请引用上述论文。

## 数据文件

分析中使用了以下数据集：

来自[英国水文办公室](https://openmldata.ukho.gov.uk/#:~:text=The%20Sentinel%2D2%20Water%20Edges,required%20for%20the%20segmentation%20mask.)的 Sentinel-2 水边数据集 (SWED) 。

该数据可根据地理空间委员会数据探索许可证获得。

## 代码文件

你可以在本文件夹中找到以下文件：

`comparison-metrics.ipynb` 主要分析文件用于应用 Canny 边缘检测、计算评估指标并创建研究论文中的所有图形。该文件还用于显示用于执行视觉分析的图形。
`utils.py` 辅助文件包含在主分析文件中执行分析所使用的函数。
`test-image-issues.ipynb` 显示 SWED 测试集中具有错误分割掩模的图像

## 结果文件

你可以找到分析中使用的以下文件：

`Visual Analysis.xlsx` 包含视觉分析的结果
`canny_evaluation_metrics.csv` 包含不同滞后阈值下的 RMSE、PSNR、SSIM 和 FOM 值以及混淆矩阵测量值