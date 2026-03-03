# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItsadug(RPackage):
	"""Interpreting Time Series and Autocorrelated Data Using GAMMs

	GAMM (Generalized Additive Mixed Modeling; Lin & Zhang, 1999)
    as implemented in the R package 'mgcv' (Wood, S.N., 2006; 2011) is a nonlinear
    regression analysis which is particularly useful for time course data such as
    EEG, pupil dilation, gaze data (eye tracking), and articulography recordings,
    but also for behavioral data such as reaction times and response data. As time
    course measures are sensitive to autocorrelation problems, GAMMs implements
    methods to reduce the autocorrelation problems. This package includes functions
    for the evaluation of GAMM models (e.g., model comparisons, determining regions
    of significance, inspection of autocorrelational structure in residuals)
    and interpreting of GAMMs (e.g., visualization of complex interactions, and
    contrasts).
	"""
	
	cran = "itsadug" 

	version("2.4.1", md5="41d9f34555c13214a4f15a131d89095a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mgcv@1.8:", type=("build", "run"))
	depends_on("r-plotfunctions@1.4:", type=("build", "run"))
