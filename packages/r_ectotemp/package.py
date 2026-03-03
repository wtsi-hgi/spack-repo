# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REctotemp(RPackage):
	"""Quantitative Estimates of Small Ectotherm Temperature Regulation
Effectiveness

	Easy and rapid quantitative estimation of small terrestrial ectotherm temperature regulation effectiveness in R. ectotemp is built on classical formulas that evaluate temperature regulation by means of various indices, inaugurated by Hertz et al. (1993) <doi: 10.1086/285573>. Options for bootstrapping and permutation testing are included to test hypotheses about divergence between organisms, species or populations.
	"""
	
	homepage = "https://CRAN.R-project.org/package=ectotemp"
	cran = "ectotemp" 

	version("0.2.0", md5="6a79f63b388de0451d44a7ee6d8d0e42")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
