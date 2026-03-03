# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaesim(RPackage):
	"""Simulation Tools for Small Area Estimation

	Tools for the simulation of data in the context of small area
    estimation. Combine all steps of your simulation - from data generation
    over drawing samples to model fitting - in one object. This enables easy
    modification and combination of different scenarios. You can store your
    results in a folder or start the simulation in parallel.
	"""
	
	homepage = "https://wahani.github.io/saeSim/"
	cran = "saeSim" 

	version("0.11.0", md5="ac61c923df55807744720206006b4971")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.2:", type=("build", "run"))
	depends_on("r-functional", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
