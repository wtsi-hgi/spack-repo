# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavaanextra(RPackage):
	"""Convenience Functions for Package 'lavaan'

	Affords an alternative, vector-based syntax to 'lavaan', as well as other 
             convenience functions such as naming paths and defining indirect
             links automatically, in addition to convenience formatting optimized
             for a publication and script sharing workflow.
	"""
	
	homepage = "https://lavaanExtra.remi-theriault.com"
	cran = "lavaanExtra" 

	version("0.2.0", md5="ba4b6e221dfeef0cd5d36656c12abc2d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
