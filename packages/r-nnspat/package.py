# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnspat(RPackage):
	"""Nearest Neighbor Methods for Spatial Patterns

	Contains the functions for testing the spatial patterns (of segregation, spatial symmetry, 
      association, disease clustering, species correspondence, and reflexivity) based on nearest neighbor relations, 
      especially using contingency tables such as 
      nearest neighbor contingency tables (Ceyhan (2010) <doi:10.1007/s10651-008-0104-x> and 
      Ceyhan (2017) <doi:10.1016/j.jkss.2016.10.002> and references therein),
      nearest neighbor symmetry contingency tables (Ceyhan (2014) <doi:10.1155/2014/698296>),
      species correspondence contingency tables and reflexivity contingency tables (Ceyhan (2018) 
      <doi:10.2436/20.8080.02.72> for two (or higher) dimensional data. 
      The package also contains functions for generating patterns of segregation, association,
      uniformity in a multi-class setting (Ceyhan (2014) <doi:10.1007/s00477-013-0824-9>), 
      and various non-random labeling patterns for disease clustering 
      in two dimensional cases (Ceyhan (2014)
      <doi:10.1002/sim.6053>), and for visualization of all these patterns 
      for the two dimensional data.
      The tests are usually (asymptotic) normal z-tests or chi-square tests.
	"""
	
	cran = "nnspat" 

	version("0.1.2", md5="0279d7b89d4f1474fa4874c9df1963e3")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pcds", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
