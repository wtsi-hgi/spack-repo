# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlide(RPackage):
	"""Global and Individual Tests for Direct Effects

	Global and individual tests for pleiotropy and direct effects in Mendelian randomization studies. Refer to J. Y. Dai, U. Peters, X. Wang, J. Kocarnik et al. AJE (2018) <doi:10.1093/aje/kwy177>.
	"""
	
	cran = "GLIDE" 

	version("1.0.5", md5="01af04bf77e8df609e1628c5d4e9897b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
