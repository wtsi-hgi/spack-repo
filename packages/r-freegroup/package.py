# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreegroup(RPackage):
	"""The Free Group

	The free group in R; juxtaposition is represented by a
  plus.  Includes inversion, multiplication by a scalar,
  group-theoretic power operation, and Tietze forms.  To cite the
  package in publications please use Hankin (2022)
  <doi:10.48550/ARXIV.2212.05883>.
	"""
	
	homepage = "https://github.com/RobinHankin/freegroup"
	cran = "freegroup" 

	version("1.1-8", md5="4afa7f6feab8d2c49b992b3ba4e94cc2")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-freealg@1.0.4:", type=("build", "run"))
	depends_on("r-magic@1.5.9:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
