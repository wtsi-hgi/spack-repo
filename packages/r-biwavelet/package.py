# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiwavelet(RPackage):
	"""Conduct Univariate and Bivariate Wavelet Analyses

	This is a port of the WTC MATLAB package written by Aslak Grinsted
    and the wavelet program written by Christopher Torrence and Gibert P.
    Compo. This package can be used to perform univariate and bivariate
    (cross-wavelet, wavelet coherence, wavelet clustering) analyses.
	"""
	
	homepage = "https://github.com/tgouhier/biwavelet"
	cran = "biwavelet" 

	version("0.20.21", md5="851649fb6673dd9ab5edb024c3123c25")

	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
