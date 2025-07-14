# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetacyto(RPackage):
	"""MetaCyto: A package for meta-analysis of cytometry data

	This package provides functions for preprocessing, automated gating and meta-analysis of cytometry data. It also provides functions that facilitate the collection of cytometry data from the ImmPort database.
	"""
	
	bioc = "MetaCyto"

	version("1.30.0", commit="d025804d8dfb487dbe31706cba0231440a6b51bc")
	version("1.24.0", commit="26465dc6c12dad9574da2fb6662173b76c8dc953")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-flowcore@1.4:", type=("build", "run"))
	depends_on("r-tidyr@0.7:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-flowsom", type=("build", "run"))
