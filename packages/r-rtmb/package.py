# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtmb(RPackage):
	"""'R' Bindings for 'TMB'

	Native 'R' interface to 'TMB' (Template Model Builder) so models can be written entirely in 'R' rather than 'C++'. Automatic differentiation, to any order, is available for a rich subset of 'R' features, including linear algebra for dense and sparse matrices, complex arithmetic, Fast Fourier Transform, probability distributions and special functions. 'RTMB' provides easy access to model fitting and validation following the principles of Kristensen, K., Nielsen, A., Berg, C. W., Skaug, H., & Bell, B. M. (2016) <DOI:10.18637/jss.v070.i05> and Thygesen, U.H., Albertsen, C.M., Berg, C.W. et al. (2017) <DOI:10.1007/s10651-017-0372-4>.
	"""
	
	homepage = "https://github.com/kaskr/RTMB"
	cran = "RTMB" 

	version("1.4", md5="2541857b04fcf8b19a3f4de60b68e931")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
