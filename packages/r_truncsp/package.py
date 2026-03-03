# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruncsp(RPackage):
	"""Semi-parametric estimators of truncated regression models

	Semi-parametric estimation of truncated linear regression models
	"""
	
	cran = "truncSP" 

	version("1.2.2", md5="a58472b6b169b376e7257d9797416dfb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-truncreg", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
