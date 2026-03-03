# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdpower(RPackage):
	"""Power Calculations for RD Designs

	The regression discontinuity (RD) design is a popular quasi-experimental design for causal inference and policy evaluation. The 'rdpower' package provides tools to perform power, sample size and MDE calculations in RD designs: rdpower() calculates the power of an RD design, rdsampsi() calculates the required sample size to achieve a desired power and rdmde() calculates minimum detectable effects. See Cattaneo, Titiunik and Vazquez-Bare (2019) <https://rdpackages.github.io/references/Cattaneo-Titiunik-VazquezBare_2019_Stata.pdf> for further methodological details.
	"""
	
	cran = "rdpower" 

	version("2.2", md5="20af5bb39f0e01bf6617d30ba5d27164")

	depends_on("r-rdrobust", type=("build", "run"))
