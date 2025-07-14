# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiamcat(RPackage):
	"""Statistical Inference of Associations between Microbial Communities And host phenoTypes

	Pipeline for Statistical Inference of Associations between Microbial Communities And host phenoTypes (SIAMCAT). A primary goal of analyzing microbiome data is to determine changes in community composition that are associated with environmental factors. In particular, linking human microbiome composition to host phenotypes such as diseases has become an area of intense research. For this, robust statistical modeling and biomarker extraction toolkits are crucially needed. SIAMCAT provides a full pipeline supporting data preprocessing, statistical association testing, statistical modeling (LASSO logistic regression) including tools for evaluation and interpretation of these models (such as cross validation, parameter selection, ROC analysis and diagnostic model plots).
	"""
	
	bioc = "SIAMCAT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SIAMCAT_2.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SIAMCAT/SIAMCAT_2.6.0.tar.gz"]

    version("2.12.0", tag="RELEASE_3_21")
	version("2.6.0", sha256="7c1d0456a178517ce6b8f951ef9642556ef91501e095b23a6eb866d39ec4a026")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-beanplot", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-liblinear", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-mlr3learners", type=("build", "run"))
	depends_on("r-mlr3tuning", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
