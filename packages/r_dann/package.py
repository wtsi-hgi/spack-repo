# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDann(RPackage):
	"""Discriminant Adaptive Nearest Neighbor Classification

	Discriminant Adaptive Nearest Neighbor Classification is a 
    variation of k nearest neighbors where the shape of the neighborhood is 
    data driven. This package implements dann and sub_dann from
    Hastie (1996) <https://web.stanford.edu/~hastie/Papers/dann_IEEE.pdf>.
	"""
	
	cran = "dann" 

	version("1.0.0", md5="5453d53f03dba3bcfbb4973f8581bcb3")

	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-fpc@2.1.11.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
