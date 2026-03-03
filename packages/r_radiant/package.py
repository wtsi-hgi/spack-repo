# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadiant(RPackage):
	"""Business Analytics using R and Shiny

	A platform-independent browser-based interface for business
    analytics in R, based on the shiny package. The application combines the
    functionality of 'radiant.data', 'radiant.design', 'radiant.basics',
    'radiant.model', and 'radiant.multivariate'.
	"""
	
	homepage = "https://github.com/radiant-rstats/radiant"
	cran = "radiant" 

	version("1.6.1", md5="c4c95ccd943e2840ea21f85588712484")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-radiant-data@1.5.1:", type=("build", "run"))
	depends_on("r-radiant-design@1.5:", type=("build", "run"))
	depends_on("r-radiant-basics@1.5:", type=("build", "run"))
	depends_on("r-radiant-model@1.5:", type=("build", "run"))
	depends_on("r-radiant-multivariate@1.5:", type=("build", "run"))
	depends_on("r-shiny@1.8:", type=("build", "run"))
	depends_on("r-import@1.1:", type=("build", "run"))
