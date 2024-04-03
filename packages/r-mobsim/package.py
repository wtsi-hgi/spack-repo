# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMobsim(RPackage):
	"""Spatial Simulation and Scale-Dependent Analysis of Biodiversity
Changes

	Simulation, analysis and sampling of spatial
    biodiversity data (May, Gerstner, McGlinn, Xiao & Chase 2017)
    <doi:10.1111/2041-210x.12986>.
    In the simulation tools user define the numbers of
    species and individuals, the species abundance distribution and species
    aggregation. Functions for analysis include species rarefaction 
    and accumulation curves, species-area relationships and the distance
    decay of similarity. 
	"""
	
	homepage = "https://github.com/MoBiodiv/mobsim"
	cran = "mobsim" 

	version("0.3.1", md5="4cc689c305c5aa0167a678f928e56d9b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-sads@0.4.1:", type=("build", "run"))
