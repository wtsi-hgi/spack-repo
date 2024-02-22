# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClump(RPackage):
	"""Clustering of Micro Panel Data

	Two-step feature-based clustering method designed for micro panel (longitudinal) data with the artificial panel data generator. See Sobisek, Stachova, Fojtik (2018) <arXiv:1807.05926>.
	"""
	
	homepage = "https://arxiv.org/ftp/arxiv/papers/1807/1807.05926.pdf"
	cran = "CluMP" 

	version("0.8.1", md5="13b55699c58d46763e5809f47e5875d2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-nbclust@3:", type=("build", "run"))
	depends_on("r-amap@0.8.16:", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
