# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNosoi(RPackage):
	"""A Forward Agent-Based Transmission Chain Simulator

	The aim of 'nosoi' (pronounced no.si) is to provide a flexible agent-based stochastic transmission chain/epidemic simulator (Lequime et al. Methods in Ecology and Evolution 11:1002-1007). It is named after the daimones of plague, sickness and disease that escaped Pandora's jar in the Greek mythology. 'nosoi' is able to take into account the influence of multiple variable on the transmission process (e.g. dual-host systems (such as arboviruses), within-host viral dynamics, transportation, population structure), alone or taken together, to create complex but relatively intuitive epidemiological simulations.
	"""
	
	homepage = "https://github.com/slequime/nosoi"
	cran = "nosoi" 

	version("1.1.2", md5="25335c2929f308af5dae10990ef25c6d")

	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster@2.8.19:", type=("build", "run"))
