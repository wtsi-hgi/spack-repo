# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTorch(RPackage):
	"""Tensors and Neural Networks with 'GPU' Acceleration

	Provides functionality to define and train neural networks similar to
    'PyTorch' by Paszke et al (2019) <arXiv:1912.01703> but written entirely in R
    using the 'libtorch' library. Also supports low-level tensor operations and
    'GPU' acceleration.
	"""
	
	homepage = "https://torch.mlverse.org/docs"
	cran = "torch" 

	version("0.12.0", md5="1e182d06b2a6ddecf95b9ee57b8df0af")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-coro@1.0.2:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-safetensors@0.1.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("py-torch", type=("build", "link", "run"))
