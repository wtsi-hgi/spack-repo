# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidysynth(RPackage):
	"""A Tidy Implementation of the Synthetic Control Method

	A synthetic control offers a way of evaluating the effect of an intervention in comparative case studies. The package makes a number of improvements when implementing the method in R. These improvements allow users to inspect, visualize, and tune the synthetic control more easily. A key benefit of a tidy implementation is that the entire preparation process for building the synthetic control can be accomplished in a single pipe.
	"""
	
	cran = "tidysynth" 

	version("0.2.0", md5="9d1870e7f77aab29a609a4e260c76a5c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
