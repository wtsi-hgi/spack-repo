# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoolnet(RPackage):
	"""Construction, Simulation and Analysis of Boolean Networks

	Functions to reconstruct, generate, and simulate synchronous, asynchronous, probabilistic, and temporal Boolean networks. Provides also functions to analyze and visualize attractors in Boolean networks <doi:10.1093/bioinformatics/btq124>.
	"""
	
	cran = "BoolNet" 

	version("2.1.9", md5="13dac13a11fb5961f559bb9d6a0d5242")

	depends_on("r-igraph@0.6:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
