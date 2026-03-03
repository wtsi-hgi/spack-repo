# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbacus(RPackage):
	"""Apps Based Activities for Communicating and Understanding
Statistics

	A set of Shiny apps for effective communication and understanding in statistics. The current version includes properties of normal distribution, properties of sampling distribution, one-sample z and t tests, two samples independent (unpaired) t test and analysis of variance.
	"""
	
	homepage = "https://shiny.abdn.ac.uk/Stats/apps/"
	cran = "ABACUS" 

	version("1.0.0", md5="50c54c4da09307cb95a70aaaa54b9fbd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-shiny@1.3.1:", type=("build", "run"))
