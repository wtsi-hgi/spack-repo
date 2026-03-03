# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlfq(RPackage):
	"""Estimating Absolute Protein Quantities from Label-Free LC-MS/MS
Proteomics Data

	Determination of absolute protein quantities is necessary for multiple applications, such as mechanistic modeling of biological systems. Quantitative liquid chromatography tandem mass spectrometry (LC-MS/MS) proteomics can measure relative protein abundance on a system-wide scale. To estimate absolute quantitative information using these relative abundance measurements requires additional information such as heavy-labeled references of known concentration. Multiple methods have been using different references and strategies; some are easily available whereas others require more effort on the users end. Hence, we believe the field might benefit from making some of these methods available under an automated framework, which also facilitates validation of the chosen strategy. We have implemented the most commonly used absolute label-free protein abundance estimation methods for LC-MS/MS modes quantifying on either MS1-, MS2-levels or spectral counts together with validation algorithms to enable automated data analysis and error estimation. Specifically, we used Monte-carlo cross-validation and bootstrapping for model selection and imputation of proteome-wide absolute protein quantity estimation. Our open-source software is written in the statistical programming language R and validated and demonstrated on a synthetic sample. 
	"""
	
	homepage = "https://github.com/aLFQ"
	cran = "aLFQ" 

	version("1.3.6", md5="a520f87481268094c11ddfb687b86eb7")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-bio3d", type=("build", "run"))
