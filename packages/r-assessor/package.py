# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssessor(RPackage):
	"""Assessment Tools for Regression Models with Discrete and
Semicontinuous Outcomes

	Provides assessment tools for regression models with discrete and semicontinuous outcomes proposed in Yang (2023) <doi:10.48550/arXiv.2308.15596>. It calculates the double probability integral transform (DPIT) residuals, constructs QQ plots of residuals and the ordered curve for assessing mean structures.
	"""
	
	homepage = "https://github.com/jhlee1408/assessor"
	cran = "assessor" 

	version("1.0.0", md5="15b0bf54367804c4b03846791862499f")

	depends_on("r-tweedie", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
