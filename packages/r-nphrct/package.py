# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNphrct(RPackage):
	"""Non-Proportional Hazards in Randomized Controlled Trials

	Perform a stratified weighted log-rank test in a randomized controlled trial. Tests can be visualized as a difference in average score on the two treatment arms. These methods are described in Magirr and Burman (2018) <arXiv:1807.11097v1>, Magirr (2020) <arXiv:2007.04767v1>, and Magirr and Jimenez (2022) <arXiv:2201.10445v1>. 
	"""
	
	cran = "nphRCT" 

	version("0.1.0", md5="c71391d37b2afbc441f0a1c4a489e041")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
