# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpeglmen(RPackage):
	"""Gamma and Exponential Generalized Linear Models with Elastic Net
Penalty

	Implements the fast iterative shrinkage-thresholding algorithm
             (FISTA) algorithm to fit a Gamma distribution with an elastic net 
             penalty as described in Chen, Arakvin and Martin (2018) 
             <arxiv:1804.07780>. An implementation for the case of the 
             exponential distribution is also available, with details available 
             in Chen and Martin (2018) <https://papers.ssrn.com/abstract_id=3085672>.
	"""
	
	cran = "RPEGLMEN" 

	version("1.1.2", md5="5ff2e2dd690f8177bbf5f383ab7a814e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rpeif", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
