# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfdm(RPackage):
	"""Simulate Forest Resources with the European Forestry Dynamics
Model

	An implementation of European Forestry Dynamics Model (EFDM) and
    an estimation algorithm for the transition probabilities.
    The EFDM is a large-scale forest model that simulates the development of
    the forest and estimates volume of wood harvested for any given forested
    area. This estimate can be broken down by, for example, species, site
    quality, management regime and ownership category.
    See Packalen et al. (2015) <doi:10.2788/153990>.
	"""
	
	homepage = "https://github.com/mikkoku/efdm"
	cran = "efdm" 

	version("0.2.1", md5="c7cdcf6485c87e81e5cd8cd96d3865d0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
