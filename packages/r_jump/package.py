# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJump(RPackage):
	"""Replicability Analysis of High-Throughput Experiments

	Implementing a computationally scalable false discovery rate control procedure for replicability analysis based on maximum of p-values. Please cite the manuscript corresponding to this package [Lyu, P. et al., (2023), <https://www.biorxiv.org/content/10.1101/2023.02.13.528417v2>].
	"""
	
	cran = "JUMP" 

	version("1.0.1", md5="b35742f5b227d71f9652e8e3840ef059")

	depends_on("r@4.1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
