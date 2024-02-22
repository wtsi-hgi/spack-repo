# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAuctionr(RPackage):
	"""Estimate First-Price Auction Model

	Estimates a first-price auction model with conditionally independent
  private values as described in MacKay (2020) <doi:10.2139/ssrn.3096534>. The
  model allows for unobserved heterogeneity that is common to all bidders in
  addition to observable heterogeneity.
	"""
	
	homepage = "https://github.com/ajmack/auctionr"
	cran = "auctionr" 

	version("0.1.0", md5="9e6119afb3348eb642535c0c72099112")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1:", type=("build", "run"))
