# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPg(RPackage):
	"""Polya Gamma Distribution Sampler

	Provides access to a high performant random distribution
    sampler for the Polya Gamma Distribution using either 'C++' headers for 
    'Rcpp' or 'RcppArmadillo' and 'R'.
	"""
	
	homepage = "https://tmsalab.github.io/pg/"
	cran = "pg" 

	version("0.2.4", md5="263a65b7f25074f9b15c1c053202c1f3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
