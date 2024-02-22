# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROwenq(RPackage):
	"""Owen Q-Function

	Evaluates the Owen Q-function for an integer value of the
    degrees of freedom, by applying Owen's algorithm (1965)
    <doi:10.1093/biomet/52.3-4.437>.  It is useful for the calculation of
    the power of equivalence tests.
	"""
	
	homepage = "https://github.com/stla/OwenQ"
	cran = "OwenQ" 

	version("1.0.7", md5="467c4958d4a0a660635d8ac514aba8e3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
