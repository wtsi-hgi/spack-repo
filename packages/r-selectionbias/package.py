# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectionbias(RPackage):
	"""Calculates Bounds for the Selection Bias for Binary Treatment
and Outcome Variables

	Computes bounds and sensitivity parameters as part of sensitivity
    analysis for selection bias. Two bounds are provided: the SV (Smith and
    VanderWeele) bound and the AF (assumption-free) bound. The SV bound assumes
    an additional dependence structure in form of a generalized M-structure
    whereas the AF bound holds for general assumptions in the potential
    outcomes framework. See Smith and VanderWeele (2019)
    <doi:10.1097/EDE.0000000000001032> and Zetterstrom and Waernbaum (2022)
    <doi:10.1515/em-2022-0108>.
	"""
	
	cran = "SelectionBias" 

	version("1.0.0", md5="b4353d8c08fb7fb3fa56ed9f67c1b67d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
