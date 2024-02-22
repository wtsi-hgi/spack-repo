# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaplus(RPackage):
	"""Robust Meta-Analysis and Meta-Regression

	Performs meta-analysis and meta-regression using standard and robust methods with confidence intervals based on the profile likelihood. Robust methods are based on alternative distributions for the random effect, either the t-distribution (Lee and Thompson, 2008 <doi:10.1002/sim.2897> or Baker and Jackson, 2008 <doi:10.1007/s10729-007-9041-8>) or mixtures of normals (Beath, 2014 <doi:10.1002/jrsm.1114>).
	"""
	
	cran = "metaplus" 

	version("1.0-4", md5="1feea92e98616835b110be6593950504")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
