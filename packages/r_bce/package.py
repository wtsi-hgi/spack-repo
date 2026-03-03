# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBce(RPackage):
	"""Bayesian Composition Estimator: Estimating Sample (Taxonomic)
Composition from Biomarker Data

	Function to estimate taxonomic compositions from biomarker data, using a Bayesian approach.
	"""
	
	cran = "BCE" 

	version("2.2.0", md5="05e3c4b32514256ea661d7013d448545")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-fme", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
