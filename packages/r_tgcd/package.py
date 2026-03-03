# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgcd(RPackage):
	"""Thermoluminescence Glow Curve Deconvolution

	Deconvolving thermoluminescence glow curves according to various 
        kinetic models (first-order, second-order, general-order, and mixed-order) using 
        a modified Levenberg-Marquardt algorithm (More, 1978) <DOI:10.1007/BFb0067700>. 
        It provides the possibility of setting constraints or fixing any of parameters. 
        It offers an interactive way to initialize parameters by clicking with a mouse on 
        a plot at positions where peak maxima should be located. The optimal estimate is 
        obtained by "trial-and-error". It also provides routines for simulating first-order, 
        second-order, and general-order glow peaks.
	"""
	
	homepage = "https://CRAN.R-project.org/package=tgcd"
	cran = "tgcd" 

	version("2.7", md5="f60ff716abc23cc84ab2e350665301eb")

	depends_on("r@3.0.1:", type=("build", "run"))
