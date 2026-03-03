# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContribution(RPackage):
	"""A Tiny Contribution Table Generator Based on 'ggplot2'

	Contribution table for credit assignment based on 'ggplot2'.
    This can improve the author contribution information in academic journals and personal CV.  
	"""
	
	homepage = "https://github.com/openbiox/contribution"
	cran = "contribution" 

	version("0.2.2", md5="97cc5f2b19644df44c9703dacd968e03")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
