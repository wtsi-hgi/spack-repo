# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTilting(RPackage):
	"""Variable Selection via Tilted Correlation Screening Algorithm

	Implements an algorithm for variable selection in high-dimensional linear regression using the "tilted correlation", a new way of measuring the contribution of each variable to the response which takes into account high correlations among the variables in a data-driven way.
	"""
	
	cran = "tilting" 

	version("1.1.1", md5="c651761491792e84a2b04f770b9be2be")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
