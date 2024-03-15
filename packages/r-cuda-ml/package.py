# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCudaMl(RPackage):
	"""R Interface for the RAPIDS cuML Suite of Libraries

	R interface for RAPIDS cuML (<https://github.com/rapidsai/cuml>),
    a suite of GPU-accelerated machine learning libraries powered by CUDA
    (<https://en.wikipedia.org/wiki/CUDA>).
	"""
	
	homepage = "https://mlverse.github.io/cuda.ml/"
	cran = "cuda.ml" 

	version("0.3.2", md5="60abac999d01323386b09adedb90ae89")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.1.4:", type=("build", "run"))
	depends_on("libcuml", type=("build", "link", "run"))
