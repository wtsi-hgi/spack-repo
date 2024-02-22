# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierportfolios(RPackage):
	"""Hierarchical Clustering-Based Portfolio Allocation Strategies

	Machine learning portfolio allocation strategies based on hierarchical clustering methods. 
 The implemented methods are:
  Hierarchical risk parity (De Prado, 2016) <DOI: 10.3905/jpm.2016.42.4.059> and
  Hierarchical clustering-based asset allocation (Raffinot, 2017) 
  <DOI: 10.3905/jpm.2018.44.2.089>.
	"""
	
	homepage = "https://github.com/ctruciosm/HierPortfolios"
	cran = "HierPortfolios" 

	version("0.1.0", md5="3b145c0a291ec945eb9ed79e3ca16bbc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-riskportfolios", type=("build", "run"))
