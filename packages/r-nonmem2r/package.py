# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonmem2r(RPackage):
	"""Loading NONMEM Output Files with Functions for Visual Predictive
Checks (VPC) and Goodness of Fit (GOF) Plots

	Loading NONMEM (NONlinear Mixed-Effect Modeling, <https://www.iconplc.com/innovation/nonmem/>) and PSN (Perl-speaks-NONMEM, <https://uupharmacometrics.github.io/PsN/>) output files to extract parameter estimates, provide visual predictive check (VPC) and goodness of fit (GOF) plots, and simulate with parameter uncertainty.
	"""
	
	cran = "nonmem2R" 

	version("0.2.4", md5="5c6b9b3e40eefdad8a4bc4db78b95bfa")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
