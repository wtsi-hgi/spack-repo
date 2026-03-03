# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHoliglm(RPackage):
	"""Holistic Generalized Linear Models

	Holistic generalized linear models (HGLMs) extend generalized linear models (GLMs) by enabling the possibility to add further constraints to the model. The 'holiglm' package simplifies estimating HGLMs using convex optimization. Additional information about the package can be found in the reference manual, the 'README' and the accompanying paper <doi:10.18637/jss.v108.i07>.
	"""
	
	cran = "holiglm" 

	version("1.0.0", md5="6f20c0a15213a0ad5486d5c9a3b5fd3d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-roi-plugin-ecos", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-roi@0.3.0:", type=("build", "run"))
