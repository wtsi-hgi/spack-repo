# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnn(RPackage):
	"""Generative Neural Networks

	Tools to set up, train, store, load, investigate and analyze
             generative neural networks. In particular, functionality for
	     generative moment matching networks is provided.
	"""
	
	cran = "gnn" 

	version("0.0-4", md5="4a05521f72998556c64a4fcc36ebff38")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-qrng", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
