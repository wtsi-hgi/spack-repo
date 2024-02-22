# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrsim(RPackage):
	"""Simulation Classes Based on Package 'distr'

	S4-classes for setting up a coherent framework for simulation within the distr
            family of packages.
	"""
	
	homepage = "http://distr.r-forge.r-project.org/"
	cran = "distrSim" 

	version("2.8.2", md5="64720fbbdb72ba2ea056cff63170fd72")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-setrng@2006.2.1:", type=("build", "run"))
	depends_on("r-distr@2.5.2:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
