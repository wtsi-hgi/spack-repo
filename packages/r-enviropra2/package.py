# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnviropra2(RPackage):
	"""Environmental Probabilistic Risk Assessment Tools

	It contains functions for dose calculation for different routes, fitting data to probability distributions, random number generation (Monte Carlo simulation) and calculation of systemic and carcinogenic risks. For more information see the publication: Barrio-Parra et al. (2019) "Human-health probabilistic risk assessment: the role of exposure factors in an urban garden scenario" <doi:10.1016/j.landurbplan.2019.02.005>. 
	"""
	
	cran = "EnviroPRA2" 

	version("1.0.1", md5="f758167784d9b4ffea3ad86ccbc62eb7", url="https://cran.r-project.org/src/contrib/EnviroPRA2_1.0.1.tar.gz")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
