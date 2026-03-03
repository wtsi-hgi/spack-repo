# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetafolio(RPackage):
	"""Metapopulation Simulations for Conserving Salmon Through
Portfolio Optimization

	A tool to simulate salmon metapopulations and apply financial
    portfolio optimization concepts. The package accompanies the paper 
    Anderson et al. (2015) <doi:10.1101/2022.03.24.485545>.
	"""
	
	homepage = "https://github.com/seananderson/metafolio"
	cran = "metafolio" 

	version("0.1.2", md5="91412b610606a8ed6035d42b9bf0648a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
