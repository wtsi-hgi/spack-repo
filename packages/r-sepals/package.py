# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSepals(RPackage):
	"""Shrinkage for Extreme Partial Least-Squares (SEPaLS)

	Regression context for the Partial Least Squares framework for 
    Extreme values. Estimations of the Shrinkage for Extreme Partial Least-Squares 
    (SEPaLS) estimators, an adaptation of the original Partial Least Squares 
    (PLS) method tailored to the extreme-value framework.
    The SEPaLS project is a joint work by Stephane Girard, Hadrien Lorenzo and 
    Julyan Arbel.
    R code to replicate the results of the paper is available at 
    <https://github.com/hlorenzo/SEPaLS_simus>.
    Extremes within PLS was already studied by one of the authors, see M 
    Bousebeta, G Enjolras, S Girard (2023) <doi:10.1016/j.jmva.2022.105101>.
	"""
	
	cran = "SEPaLS" 

	version("0.1.0", md5="00d5088530983733fe299e700785c0cc")

	depends_on("r@3.5:", type=("build", "run"))
