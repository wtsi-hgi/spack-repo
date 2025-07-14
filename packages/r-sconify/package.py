# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSconify(RPackage):
	"""A toolkit for performing KNN-based statistics for flow and mass cytometry data

	This package does k-nearest neighbor based statistics and visualizations with flow and mass cytometery data. This gives tSNE maps"fold change" functionality and provides a data quality metric by assessing manifold overlap between fcs files expected to be the same. Other applications using this package include imputation, marker redundancy, and testing the relative information loss of lower dimension embeddings compared to the original manifold.
	"""
	
	bioc = "Sconify"

	version("1.28.0", commit="77b3a46ba6b7d7088aa239d99395f448c493221c")
	version("1.22.0", commit="ffdb315907302882bf34343dc726db91d78baaa9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
