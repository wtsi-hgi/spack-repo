# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlz(RPackage):
	"""Mean Length-Based Estimators of Mortality using TMB

	Estimation functions and diagnostic tools for mean length-based total mortality estimators based on Gedamke and Hoenig (2006) <doi:10.1577/T05-153.1>.
	"""
	
	cran = "MLZ" 

	version("0.1.4", md5="969b1a6967ef9cc4957d058f4c11a106")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
