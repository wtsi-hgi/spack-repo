# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSglr(RPackage):
	"""Sequential Generalized Likelihood Ratio Decision Boundaries
Proposed by Shih, Lai, Heyse and Chen (2010,
<doi:10.1002/Sim.4036>)

	We provide functions for computing the decision boundaries for pre-licensure vaccine trials using the Generalized Likelihood Ratio tests proposed by Shih, Lai, Heyse and Chen (2010, <doi:10.1002/sim.4036>).
	"""
	
	cran = "sglr" 

	version("0.8", md5="0ddc0953b3bc366329dc9a352cd64eb5")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
