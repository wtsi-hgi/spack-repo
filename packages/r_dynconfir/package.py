# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynconfir(RPackage):
	"""Dynamic Models for Confidence and Response Time Distributions

	Provides density functions for the joint distribution of
    choice, response time and confidence for discrete confidence judgments
    as well as functions for parameter fitting, prediction and simulation
    for various dynamical models of decision confidence.  All models are
    explained in detail by Hellmann et al.  (2023;
    Preprint available at <https://osf.io/9jfqr/>, published version: <doi:10.1037/rev0000411>).  Implemented models are the dynaViTE model, 
    dynWEV model, the 2DSD model (Pleskac & Busemeyer, 2010, <doi:10.1037/a0019737>),
    and various race models.  C++ code for dynWEV and 2DSD is based on the
    'rtdists' package by Henrik Singmann.
	"""
	
	homepage = "https://github.com/SeHellmann/dynConfiR"
	cran = "dynConfiR" 

	version("0.0.4", md5="24377f0b058bfbd63cab75df910eb5ce")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
