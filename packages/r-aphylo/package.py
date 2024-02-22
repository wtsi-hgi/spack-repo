# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAphylo(RPackage):
	"""Statistical Inference and Prediction of Annotations in
Phylogenetic Trees

	Implements a parsimonious evolutionary model to analyze and
  predict gene-functional annotations in phylogenetic trees as described in Vega
  Yon et al. (2021) <doi:10.1371/journal.pcbi.1007948>. Focusing on
  computational efficiency, 'aphylo' makes it possible to estimate pooled
  phylogenetic models, including thousands (hundreds) of annotations (trees) in
  the same run. The package also provides the tools for visualization of
  annotated phylogenies, calculation of posterior probabilities (prediction)
  and goodness-of-fit assessment featured in Vega Yon et al. (2021).
	"""
	
	homepage = "https://github.com/USCbiostats/aphylo"
	cran = "aphylo" 

	version("0.3-3", md5="5b84af609f9618c7f1cb2bab36b23c19")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-fmcmc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
