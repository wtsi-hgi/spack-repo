# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsl(RPackage):
	"""Site Percolation on Square Lattices (SPSL)

	Provides basic functionality for labeling 
        iso- & anisotropic percolation clusters on 2D & 3D square lattices 
        with various lattice sizes, occupation probabilities, von Neumann & 
        Moore (1,d)-neighborhoods, and random variables weighting 
        the percolation lattice sites.
	"""
	
	homepage = "https://cran.r-project.org/package=SPSL"
	cran = "SPSL" 

	version("0.1-9", md5="cd001f0334239b7715cca1ecabccc3ee")

