# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHierportfolios(RPackage):
	"""Hierarchical Clustering-Based Portfolio Allocation Strategies

	Machine learning portfolio allocation strategies based on hierarchical clustering methods. 
 The implemented methods are:
  Hierarchical risk parity (De Prado, 2016) <DOI: 10.3905/jpm.2016.42.4.059>.
  Hierarchical clustering-based asset allocation (Raffinot, 2017)  
  <DOI: 10.3905/jpm.2018.44.2.089>.
  Hierarchical equal risk contribution portfolio (Raffinot, 2018)
  <DOI: 10.2139/ssrn.3237540>.
  A Constrained Hierarchical Risk Parity Algorithm with Cluster-based Capital Allocation (Pfitzingera and Katzke, 2019)
  <https://www.ekon.sun.ac.za/wpapers/2019/wp142019/wp142019.pdf>.
	"""
	
	homepage = "https://github.com/ctruciosm/HierPortfolios"
	cran = "HierPortfolios" 

	version("1.0.0", md5="dfa668a3d7d3529ea9004f8a0b32eb5a")
	version("0.1.0", md5="3b145c0a291ec945eb9ed79e3ca16bbc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
