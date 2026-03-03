# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathmodelfit(RPackage):
	"""Path Component Fit Indices for Latent Structural Equation Models

	Functions for computing fit indices for 
    evaluating the path component of latent variable structural equation models. 
    Available fit indices include RMSEA-P and NSCI-P originally presented and evaluated 
    by Williams and O'Boyle (2011) <doi:10.1177/1094428110391472> and demonstrated by 
    O'Boyle and Williams (2011) <doi:10.1037/a0020539> and Williams, O'Boyle, & Yu (2020) 
    <doi:10.1177/1094428117736137>. Also included are fit indices described by 
    Hancock and Mueller (2011) <doi:10.1177/0013164410384856>.
	"""
	
	cran = "pathmodelfit" 

	version("1.0.5", md5="3e07f5d1f5a3aa2b07aa50f0bd4825b9")

	depends_on("r-lavaan", type=("build", "run"))
