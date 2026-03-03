# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpqplan(RPackage):
	"""Process Performance Qualification (PPQ) Plans in Chemistry,
Manufacturing and Controls (CMC) Statistical Analysis

	Assessment for statistically-based PPQ sampling plan, including calculating the passing probability, optimizing the baseline and high performance cutoff points, visualizing the PPQ plan and power dynamically. The analytical idea is based on the simulation methods from the textbook Burdick, R. K., LeBlond, D. J., Pfahler, L. B., Quiroz, J., Sidor, L., Vukovinsky, K., & Zhang, L. (2017). Statistical Methods for CMC Applications. In Statistical Applications for Chemistry, Manufacturing and Controls (CMC) in the Pharmaceutical Industry (pp. 227-250). Springer, Cham.
	"""
	
	homepage = "https://allenzhuaz.github.io/PPQplan/"
	cran = "PPQplan" 

	version("1.1.0", md5="b849f7a9e2aebeee5a91ad172be168d7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
