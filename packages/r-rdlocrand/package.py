# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdlocrand(RPackage):
	"""Local Randomization Methods for RD Designs

	The regression discontinuity (RD) design is a popular quasi-experimental design for causal inference and policy evaluation. Under the local randomization approach, RD designs can be interpreted as randomized experiments inside a window around the cutoff. This package provides tools to perform randomization inference for RD designs under local randomization: rdrandinf() to perform hypothesis testing using randomization inference, rdwinselect() to select a window around the cutoff in which randomization is likely to hold, rdsensitivity() to assess the sensitivity of the results to different window lengths and null hypotheses and rdrbounds() to construct Rosenbaum bounds for sensitivity to unobserved confounders. See Cattaneo, Titiunik and Vazquez-Bare (2016) <https://rdpackages.github.io/references/Cattaneo-Titiunik-VazquezBare_2016_Stata.pdf> for further methodological details.
	"""
	
	cran = "rdlocrand" 

	version("1.0", md5="4ea59111a2a79a8e58535e065e2b7e34")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
