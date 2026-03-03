# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbnetworkma(RPackage):
	"""Contrast-Based Bayesian Network Meta Analysis

	A function that facilitates fitting three types of models 
    for contrast-based Bayesian Network Meta Analysis.  The first model is that which
    is described in Lu and Ades (2006) <doi:10.1198/016214505000001302>.  The other two 
    models are based on a Bayesian nonparametric methods that permit ties when comparing 
    treatment or for a treatment effect to be exactly equal to zero. In addition to the 
    model fits, the package provides a summary of the interplay  between treatment 
    effects based on the procedure described in Barrientos, Page, and Lin (2023)
    <doi:10.48550/arXiv.2207.06561>.
	"""
	
	cran = "CBnetworkMA" 

	version("0.1.0", md5="d1afab29764f167a638a7988ad4f06ca")

	depends_on("r@4.2:", type=("build", "run"))
