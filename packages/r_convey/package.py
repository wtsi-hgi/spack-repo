# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvey(RPackage):
	"""Income Concentration Analysis with Complex Survey Samples

	Variance estimation on indicators of income concentration and
    poverty using complex sample survey designs. Wrapper around the
    'survey' package.
	"""
	
	homepage = "https://guilhermejacob.github.io/context/"
	cran = "convey" 

	version("1.0.0", md5="6687e3a522233c296c2fae6751df5d47")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survey@4.2.1:", type=("build", "run"))
