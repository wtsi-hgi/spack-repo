# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPac(RPackage):
	"""Partition-Assisted Clustering and Multiple Alignments of
Networks

	Implements partition-assisted clustering and multiple alignments of networks. It 1) utilizes partition-assisted clustering to find robust and accurate clusters and 2) discovers coherent relationships of clusters across multiple samples. It is particularly useful for analyzing single-cell data set. Please see Li et al. (2017) <doi:10.1371/journal.pcbi.1005875> for detail method description.
	"""
	
	homepage = "https://doi.org/10.1371/journal.pcbi.1005875"
	cran = "PAC" 

	version("1.1.4", md5="54e9a0ed05a36f8e2d2f0d9ad4af63ba")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-parmigene", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
