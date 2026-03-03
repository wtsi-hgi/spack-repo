# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustermole(RPackage):
	"""Unbiased Single-Cell Transcriptomic Data Cell Type
Identification

	Assignment of cell type labels to single-cell RNA sequencing (scRNA-seq) clusters is often a time-consuming process that involves manual inspection of the cluster marker genes complemented with a detailed literature search. This is especially challenging when unexpected or poorly described populations are present. The clustermole R package provides methods to query thousands of human and mouse cell identity markers sourced from a variety of databases.
	"""
	
	homepage = "https://igordot.github.io/clustermole/"
	cran = "clustermole" 

	version("1.1.1", md5="9c170570625f73839da6c71c17b17512")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-gsva@1.50:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-singscore", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
