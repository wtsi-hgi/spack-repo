# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsd(RPackage):
	"""Adaptive, Sine-Multitaper Power Spectral Density and Cross
Spectrum Estimation

	Produces power spectral density estimates through iterative
    refinement of the optimal number of sine-tapers at each frequency. This
    optimization procedure is based on the method of Riedel and Sidorenko
    (1995), which minimizes the Mean Square Error (sum of variance and bias)
    at each frequency, but modified for computational stability. The same
    procedure can now be used to calculate the cross spectrum (multivariate
    analyses).
	"""
	
	homepage = "https://github.com/abarbour/psd"
	cran = "psd" 

	version("2.1.1", md5="08ec2ff55233e983b7932ad783414c69")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
