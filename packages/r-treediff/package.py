# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreediff(RPackage):
	"""Testing Differences Between Families of Trees

	Perform test to detect differences in structure between families of
             trees. The method is based on cophenetic distances and aggregated
             Student's tests.
	"""
	
	homepage = "https://forgemia.inra.fr/scales/treediff"
	cran = "treediff" 

	version("0.2.1", md5="45a11d08b41e1bc65d9d65b6160efaed")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-adjclust", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-csaw", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-hicdoc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
