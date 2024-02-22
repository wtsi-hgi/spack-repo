# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgst(RPackage):
	"""Informative Gene Selection Tool

	Mining informative genes with certain biological meanings are important for clinical diagnosis of disease and discovery of disease mechanisms in plants and animals. This process involves identification of relevant genes and removal of redundant genes as much as possible from a whole gene set. This package selects the informative genes related to a specific trait using gene expression dataset. These trait specific genes are considered as informative genes. This package returns the informative gene set from the high dimensional gene expression data using a combination of methods SVM and MRMR (for feature selection) with bootstrapping procedure. 
	"""
	
	cran = "IGST" 

	version("0.1.0", md5="32c0c315830ddf0c0d163769140bcd7c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-bootmrmr", type=("build", "run"))
