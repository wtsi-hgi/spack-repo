# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyedsurvey(RPackage):
	"""Integration of 'dplyr' and 'ggplot2' with 'EdSurvey'

	Takes objects of class edsurvey.data.frame and converts them to a data.frame within the calling environment of 'dplyr' and 'ggplot2' functions. Additionally, for plotting with 'ggplot2', users can map aesthetics to subject scales and all plausible values will be used. This package supports student level data; to work with school or teacher level data, see '?EdSurvey::getData'.
	"""
	
	cran = "tidyEdSurvey" 

	version("0.1.2", md5="2ce13405110792cdbb2f00806a6f7f43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-edsurvey@4.0.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
