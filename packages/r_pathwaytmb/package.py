# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathwaytmb(RPackage):
	"""Pathway Based Tumor Mutational Burden

	A systematic bioinformatics tool to develop a new pathway-based gene panel for tumor mutational burden (TMB) assessment (pathway-based tumor mutational burden, PTMB), using somatic mutations files in an efficient manner from either The Cancer Genome Atlas sources or any in-house studies as long as the data is in mutation annotation file (MAF) format. Besides, we develop a multiple machine learning method using the sample's PTMB profiles to identify cancer-specific dysfunction pathways, which can be a biomarker of prognostic and predictive for cancer immunotherapy.
	"""
	
	cran = "pathwayTMB" 

	version("0.1.3", md5="83657c83082187cc31cf999edba5b0e5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
