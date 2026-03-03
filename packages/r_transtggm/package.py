# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTranstggm(RPackage):
	"""Transfer Learning for Tensor Graphical Models

	Tensor Gaussian graphical models (GGMs) have important applications in numerous areas, which can interpret conditional independence structures within tensor data. Yet, the available tensor data in one single study is often limited due to high acquisition costs. 
             Although relevant studies can provide additional data, it remains an open question how to pool such heterogeneous data. This package implements a transfer learning framework for tensor GGMs, which takes full advantage of informative auxiliary domains even when non-informative auxiliary domains are present, benefiting from the carefully designed data-adaptive weights. 
             Reference: 
             Ren, M., Zhen Y., and Wang J. (2022). "Transfer learning for tensor graphical models" <arXiv:2211.09391>.
	"""
	
	cran = "TransTGGM" 

	version("1.0.0", md5="4ad7b694375f6a7279a6b9054b6ba686")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-tlasso", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
