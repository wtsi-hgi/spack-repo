# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvyvgam(RPackage):
	"""Design-Based Inference in Vector Generalised Linear Models

	Provides inference based on the survey package for the wide range of parametric models in the 'VGAM' package.
	"""
	
	cran = "svyVGAM" 

	version("1.2", md5="0c075246ea76ffae12520ccbce419143")

	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
