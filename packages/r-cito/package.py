# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCito(RPackage):
	"""Building and Training Neural Networks

	Building and training custom neural networks in the typical R syntax. The 'torch' package is used for numerical calculations, which allows for training on CPU as well as on a graphics card. 
	"""
	
	homepage = "https://citoverse.github.io/cito/"
	cran = "cito" 

	version("1.0.2", md5="7b48f67506c33fe27fe75ee09d2f9fcd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-parabar", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
