# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootstepaic(RPackage):
	"""Bootstrap stepAIC

	Model selection by bootstrapping the stepAIC() procedure.
	"""
	
	cran = "bootStepAIC" 

	version("1.3-0", md5="15ef641995bff2ede453c866b1572315")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
