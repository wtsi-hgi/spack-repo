# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransformer(RPackage):
	"""Implementation of Transformer Deep Neural Network with Vignettes

	Transformer is a Deep Neural Network Architecture based i.a. on the Attention mechanism (Vaswani et al. (2017) <doi:10.48550/arXiv.1706.03762>). 
	"""
	
	cran = "transformer" 

	version("0.2.0", md5="526ad16803d17acd3259cd3f3546822c")

	depends_on("r-attention@0.4:", type=("build", "run"))
