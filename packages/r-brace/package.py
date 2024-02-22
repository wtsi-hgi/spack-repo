# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrace(RPackage):
	"""Bias Reduction Through Analysis of Competing Events (BRACE)

	Adjusting the bias due to residual confounding (often called
    treatment selection bias) in estimating the treatment effect in a
    proportional hazard model, as described in Williamson et al.
    (2022) <doi:10.1158/1078-0432.ccr-21-2468>.
	"""
	
	cran = "BRACE" 

	version("0.1.0", md5="9bba79ef35282d1c963e61f141df384b")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
