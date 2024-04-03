# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncosubtype(RPackage):
	"""Predict Cancer Subtypes Based on TCGA Data using Machine
Learning Method

	Provide functionality for cancer subtyping using nearest centroids or machine learning methods based on TCGA data.
	"""
	
	homepage = "https://github.com/DadongZ/OncoSubtype"
	cran = "OncoSubtype" 

	version("1.0.0", md5="b14d62ce3f262c78ecb619faf653f7cd")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r@3.63:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
