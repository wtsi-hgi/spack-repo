# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVectorwavelet(RPackage):
	"""Vector Wavelet Coherence for Multiple Time Series

	New wavelet methodology (vector wavelet coherence) (Oygur, T., Unal, G, 2020 <doi:10.1007/s40435-020-00706-y>) 
  to handle dynamic co-movements of multivariate time series via extending multiple and quadruple wavelet coherence methodologies. 
  This package can be used to perform multiple wavelet coherence, quadruple wavelet coherence, and n-dimensional vector wavelet coherence analyses.
	"""
	
	homepage = "https://github.com/toygur/vectorwavelet"
	cran = "vectorwavelet" 

	version("0.1.0", md5="67d70438d516d43a2c83d9084e4bcf7a")

	depends_on("r-biwavelet@0.20.19:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
