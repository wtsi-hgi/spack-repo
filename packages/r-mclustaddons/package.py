# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMclustaddons(RPackage):
	"""Addons for the 'mclust' Package

	Extend the functionality of the 'mclust' package for 
  Gaussian finite mixture modeling by including: 
  density estimation for data with bounded support 
  (Scrucca, 2019 <doi:10.1002/bimj.201800174>);
  modal clustering using MEM (Modal EM) algorithm for Gaussian mixtures 
  (Scrucca, 2021 <doi:10.1002/sam.11527>);
  entropy estimation via Gaussian mixture modeling
  (Robin & Scrucca, 2023 <doi:10.1016/j.csda.2022.107582>).
	"""
	
	homepage = "https://mclust-org.github.io/mclustAddons/"
	cran = "mclustAddons" 

	version("0.8", md5="82ddb64a3873cb3c7728ceb46afbe55a")
	version("0.7.2", md5="5f1ab6d66258a80e462b2ac4eab8891a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mclust@6.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10:", type=("build", "run"))
