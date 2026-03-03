# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMareymap(RPackage):
	"""Estimation of Meiotic Recombination Rates Using Marey Maps

	Local recombination rates are graphically estimated across a genome using Marey maps.
	"""
	
	homepage = "https://lbbe.univ-lyon1.fr/fr/mareymap"
	cran = "MareyMap" 

	version("1.3.7", md5="c1fe150ed54e670a8287bd6d9d7c768d")

	depends_on("r@2.10:", type=("build", "run"))
