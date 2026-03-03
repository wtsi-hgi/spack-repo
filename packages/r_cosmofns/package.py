# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosmofns(RPackage):
	"""Functions for Cosmological Distances, Times, Luminosities, Etc

	Package encapsulates standard expressions for distances, times, luminosities, and other quantities useful in observational cosmology, including molecular line observations.  Currently coded for a flat universe only.
	"""
	
	cran = "cosmoFns" 

	version("1.1-1", md5="b85afa5cf08936382f601f3e1ff6079d")

