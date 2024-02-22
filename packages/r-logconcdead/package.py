# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogconcdead(RPackage):
	"""Log-Concave Density Estimation in Arbitrary Dimensions

	Software for computing a log-concave (maximum likelihood) estimator for independent and identically distributed data in any number of dimensions. For a detailed description of the method see Cule, Samworth and Stewart (2010, Journal of Royal Statistical Society Series B, <doi:10.1111/j.1467-9868.2010.00753.x>).
	"""
	
	cran = "LogConcDEAD" 

	version("1.6-9", md5="1fc896291a11ee245107defd40767e37")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
