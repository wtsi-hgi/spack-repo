# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidysq(RPackage):
	"""Tidy Processing and Analysis of Biological Sequences

	A tidy approach to analysis of biological sequences. All processing and data-storage functions are heavily optimized to allow the fastest and most efficient data storage.
	"""
	
	homepage = "https://github.com/BioGenies/tidysq"
	cran = "tidysq" 

	version("1.1.3", md5="4d2faaf01ccbe0122e7b15279d21fd9e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-checkmate@1.9:", type=("build", "run"))
	depends_on("r-cli@2:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-pillar@1.4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
