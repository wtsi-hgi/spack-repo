# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaskexact(RPackage):
	"""Exact Calculation of Basket Trial Operating Characteristics

	Calculates the exact operating characteristics of a single-stage
    basket trial with the design of
	Fujikawa, K., Teramukai, S., Yokota, I., & Daimon, T. (2020). <doi:10.1002/bimj.201800404>.
	"""
	
	homepage = "https://github.com/lbau7/baskexact"
	cran = "baskexact" 

	version("0.1.0", md5="f775cd078e8758ba77c57f26b3a93859")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
