# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothsurv(RPackage):
	"""Survival Regression with Smoothed Error Distribution

	Contains, as a main contribution, a function to fit
             a regression model with possibly right, left or interval
             censored observations and with the error distribution
             expressed as a mixture of G-splines. Core part
             of the computation is done in compiled 'C++' written
             using the 'Scythe' Statistical Library Version 0.3.
	"""
	
	homepage = "https://msekce.karlin.mff.cuni.cz/~komarek/"
	cran = "smoothSurv" 

	version("2.6", md5="e84b8cfef6ecaac3345ac17e883c696c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
