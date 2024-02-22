# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimriv(RPackage):
	"""Simulating Multistate Movements in River/Heterogeneous
Landscapes

	Provides functions to generate and analyze spatially-explicit individual-based multistate movements in rivers,
  heterogeneous and homogeneous spaces. This is done by incorporating landscape bias on local behaviour, based on
  resistance rasters. Although originally conceived and designed to simulate trajectories of species constrained to
  linear habitats/dendritic ecological networks (e.g. river networks), the simulation algorithm is built to be
  highly flexible and can be applied to any (aquatic, semi-aquatic or terrestrial) organism, independently on the
  landscape in which it moves. Thus, the user will be able to use the package to simulate movements either in
  homogeneous landscapes, heterogeneous landscapes (e.g. semi-aquatic animal moving mainly along rivers but also using
  the matrix), or even in highly contrasted landscapes (e.g. fish in a river network). The algorithm and its input
  parameters are the same for all cases, so that results are comparable. Simulated trajectories can then be used as
  mechanistic null models (Potts & Lewis 2014, <DOI:10.1098/rspb.2014.0231>) to test a variety of 'Movement Ecology'
  hypotheses (Nathan et al. 2008, <DOI:10.1073/pnas.0800375105>), including landscape effects (e.g. resources, 
  infrastructures) on animal movement and species site fidelity, or for predictive purposes (e.g. road mortality risk,
  dispersal/connectivity). The package should be relevant to explore a broad spectrum of ecological phenomena, such as
  those at the interface of animal behaviour, management, landscape and movement ecology, disease and invasive species
  spread, and population dynamics.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "SiMRiv" 

	version("1.0.6", md5="0e384f98b845f83772581b6934ec3bad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-mco", type=("build", "run"))
