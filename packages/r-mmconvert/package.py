# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmconvert(RPackage):
	"""Mouse Map Converter

	Convert mouse genome positions between the build 39 physical map and the genetic map of Cox et al. (2009) <doi:10.1534/genetics.109.105486>.
	"""
	
	homepage = "https://github.com/rqtl/mmconvert"
	cran = "mmconvert" 

	version("0.10", md5="387c35377da9020645449ab71c53ff5f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
