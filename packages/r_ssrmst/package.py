# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsrmst(RPackage):
	"""Sample Size Calculation using Restricted Mean Survival Time

	Calculates the power and sample size based on the difference in Restricted Mean Survival Time.
	"""
	
	cran = "SSRMST" 

	version("0.1.1", md5="99e609e93292c4ac8cc53f52afb8b938")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survrm2", type=("build", "run"))
