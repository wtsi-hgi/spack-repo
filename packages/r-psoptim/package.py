# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsoptim(RPackage):
	"""Particle Swarm Optimization

	Particle swarm optimization - a basic variant.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "psoptim" 

	version("1.0", md5="346d424cd9b9f13ddc2a613e04f56de0")

	depends_on("r@2:", type=("build", "run"))
