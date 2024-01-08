# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RMhurdle(RPackage):
	"""Multiple Hurdle Tobit Models

	Estimation of models with zero left-censored variables.
             Null values may be caused by a selection process
	     Cragg (1971) <doi:10.2307/1909582>, insufficient resources
	     Tobin (1958) <doi:10.2307/1907382> or infrequency of purchase
	     Deaton and Irish (1984) <doi:10.1016/0047-2727(84)90067-7>.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "mhurdle" 

	version("1.3-0", md5="a02c785725876379db940821069cefc6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-truncreg", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-prediction", type=("build", "run"))
	depends_on("r-margins", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
