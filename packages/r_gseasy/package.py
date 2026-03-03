# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGseasy(RPackage):
	"""Gene Set Enrichment Analysis in R

	R-interface to C++ implementation of the rank/score permutation based GSEA test (Subramanian et al 2005 <doi: 10.1073/pnas.0506580102>).
	"""
	
	cran = "gsEasy" 

	version("1.5", md5="9890c0fee14b92de3028f4711f64a985")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ontologyindex@2:", type=("build", "run"))
