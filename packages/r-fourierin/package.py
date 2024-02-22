# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFourierin(RPackage):
	"""Computes Numeric Fourier Integrals

	Computes Fourier integrals of functions of one and two variables using the Fast Fourier transform. The Fourier transforms must be evaluated on a regular grid for fast evaluation.
	"""
	
	homepage = "https://github.com/gbasulto/fourierin"
	cran = "fourierin" 

	version("0.2.5", md5="0f07a675e7f0270750edcb8f3e3e9247")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
