# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtde(RPackage):
	"""Robust Tail Dependence Estimation

	Robust tail dependence estimation for bivariate models. This package is based on two papers by the authors:'Robust and bias-corrected estimation of the coefficient of tail dependence' and 'Robust and bias-corrected estimation of probabilities of extreme failure sets'. This work was supported by a research grant (VKR023480) from VILLUM FONDEN and an international project for scientific cooperation (PICS-6416).
	"""
	
	cran = "RTDE" 

	version("0.2-1", md5="4ace850d6901a0bf9f701b177bb587bd")

	depends_on("r@3:", type=("build", "run"))
