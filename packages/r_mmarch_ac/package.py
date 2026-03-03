# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmarchAc(RPackage):
	"""Processing of Accelerometry Data with 'GGIR' in mMARCH

	Mobile Motor Activity Research Consortium for Health (mMARCH) is a collaborative network of studies of clinical and community samples that employ common clinical, biological, and digital mobile measures across involved studies. One of the main scientific goals of mMARCH sites is developing a better understanding of the inter-relationships between accelerometry-measured physical activity (PA), sleep (SL), and circadian rhythmicity (CR) and mental and physical health in children, adolescents, and adults. Currently, there is no consensus on a standard procedure for a data processing pipeline of raw accelerometry data, and few open-source tools to facilitate their development. The R package 'GGIR' is the most prominent open-source software package that offers great functionality and tremendous user flexibility to process raw accelerometry data. However, even with 'GGIR', processing done in a harmonized and reproducible fashion requires a non-trivial amount of expertise combined with a careful implementation. In addition, novel accelerometry-derived features of PA/SL/CR capturing multiscale, time-series, functional, distributional and other complimentary aspects of accelerometry data being constantly proposed and become available via non-GGIR R implementations.  To address these issues, mMARCH developed a streamlined harmonized and reproducible pipeline for loading and cleaning raw accelerometry data, extracting features available through 'GGIR' as well as through non-GGIR R packages, implementing several data and feature quality checks, merging all features of PA/SL/CR together, and performing multiple analyses including Joint Individual Variation Explained (JIVE), an unsupervised machine learning dimension reduction technique that identifies latent factors capturing joint across and individual to each of three domains of PA/SL/CR.  In detail, the pipeline generates all necessary R/Rmd/shell files for data processing after running 'GGIR' (v2.4.0) for accelerometer data. In module 1, all csv files in the 'GGIR' output directory were read, transformed and then merged. In module 2, the 'GGIR' output files were checked and summarized in one excel sheet. In module 3, the merged data was cleaned according to the number of valid hours on each night and the number of valid days for each subject. In module 4, the cleaned activity data was imputed by the average Euclidean norm minus one (ENMO) over all the valid days for each subject. Finally, a comprehensive report of data processing was created using Rmarkdown, and the report includes few exploratory plots and multiple commonly used features extracted from minute level actigraphy data.  Reference: Guo W, Leroux A, Shou S, Cui L, Kang S, Strippoli MP, Preisig M, Zipunnikov V, Merikangas K (2022) Processing of accelerometry data with GGIR in Motor Activity Research Consortium for Health (mMARCH) Journal for the Measurement of Physical Behaviour, 6(1): 37-44.
	"""
	
	homepage = "https://github.com/WeiGuoNIMH/mMARCH.AC"
	cran = "mMARCH.AC" 

	version("2.9.2.0", md5="dcfbd8842984afaae48d058f069c6b71")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-refund", type=("build", "run"))
	depends_on("r-denseflmm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-cosinor", type=("build", "run"))
	depends_on("r-cosinor2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-accelerometry", type=("build", "run"))
	depends_on("r-actcr", type=("build", "run"))
	depends_on("r-actfrag", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-ggir", type=("build", "run"))
