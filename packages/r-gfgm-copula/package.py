# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfgmCopula(RPackage):
	"""Generalized Farlie-Gumbel-Morgenstern Copula

	Compute bivariate dependence measures and perform bivariate competing risks analysis under the generalized Farlie-Gumbel-Morgenstern (FGM) copula. See Shih and Emura (2018) <doi:10.1007/s00180-018-0804-0> and Shih and Emura (2019) <doi:10.1007/s00362-016-0865-5> for details.
	"""
	
	cran = "GFGM.copula" 

	version("1.0.4", md5="a8580d4d63ef1bc7127b2cd4a77513bd")

	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-compound-cox", type=("build", "run"))
	depends_on("r-joint-cox", type=("build", "run"))
