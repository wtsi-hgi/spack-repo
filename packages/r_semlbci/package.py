# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemlbci(RPackage):
	"""Likelihood-Based Confidence Interval in Structural Equation
Models

	Forms likelihood-based confidence intervals
    (LBCIs) for parameters in structural equation modeling,
    introduced in Cheung and Pesigan (2023)
    <doi:10.1080/10705511.2023.2183860>. Currently
    implements the algorithm illustrated by Pek and Wu
    (2018) <doi:10.1037/met0000163>, and supports the robust
    LBCI proposed by Falk (2018)
    <doi:10.1080/10705511.2017.1367254>.
	"""
	
	homepage = "https://sfcheung.github.io/semlbci/"
	cran = "semlbci" 

	version("0.10.4", md5="7e239dd7c3d55cda0016631603236665")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lavaan@0.6.13:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
