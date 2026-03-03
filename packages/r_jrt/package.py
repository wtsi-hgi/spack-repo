# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJrt(RPackage):
	"""Item Response Theory Modeling and Scoring for Judgment Data

	Psychometric analysis and scoring of judgment data using polytomous Item-Response Theory (IRT) models, as described in Myszkowski and Storme (2019) <doi:10.1037/aca0000225> and Myszkowski (2021) <doi:10.1037/aca0000287>. A function is used to automatically compare and select models, as well as to present a variety of model-based statistics. Plotting functions are used to present category curves, as well as information, reliability and standard error functions.
	"""
	
	cran = "jrt" 

	version("1.1.2", md5="314b5c4a82f28f85450330555efabf5d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-directlabels@2021.1.13:", type=("build", "run"))
	depends_on("r-mirt@1.34:", type=("build", "run"))
	depends_on("r-psych@2.1.9:", type=("build", "run"))
	depends_on("r-irr@0.84.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-ggsci@2.9:", type=("build", "run"))
