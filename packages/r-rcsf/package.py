# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcsf(RPackage):
	"""Airborne LiDAR Filtering Method Based on Cloth Simulation

	Cloth Simulation Filter (CSF) is an airborne LiDAR (Light Detection and Ranging) ground 
    points filtering algorithm  which is based on cloth simulation. It tries to simulate the interactions
    between the cloth nodes and the corresponding LiDAR points, the locations of the cloth nodes can be
    determined to generate an approximation of the ground surface <https://www.mdpi.com/2072-4292/8/6/501/htm>.
	"""
	
	cran = "RCSF" 

	version("1.0.2", md5="6f40101ebfa66f927c40b825717acd35")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
