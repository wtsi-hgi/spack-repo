# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectionbias(RPackage):
	"""Calculates Bounds for the Selection Bias for Binary Treatment
and Outcome Variables

	Computes bounds and sensitivity parameters as part of sensitivity 
    analysis for selection bias. Different bounds are provided: the SV (Smith 
    and VanderWeele), AF (assumption-free) bound, GAF (generalized 
    AF), and CAF (counterfactual AF) bounds. The calculation of the sensitivity 
    parameters for the SV and GAF bounds assume an additional dependence 
    structure in form of a generalized M-structure. The bounds can be
    calculated for any structure as long as the necessary assumptions hold. See 
    Smith and VanderWeele (2019) <doi:10.1097/EDE.0000000000001032>, 
    Zetterstrom and Waernbaum (2022) <doi:10.1515/em-2022-0108> and
    Zetterstrom (2024) <doi:10.1515/em-2023-0033>.
	"""
	
	homepage = "https://github.com/stizet/SelectionBias"
	cran = "SelectionBias" 

	version("2.0.0", md5="bdc817925e565e51cc4fbaca72f129f1")
	version("1.0.0", md5="b4353d8c08fb7fb3fa56ed9f67c1b67d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
