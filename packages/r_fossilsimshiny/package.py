# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFossilsimshiny(RPackage):
	"""Shiny Application for 'FossilSim'

	A shiny application based on 'FossilSim'. Used for simulating
    tree, taxonomic and fossil data under mechanistic models of speciation,
    preservation and sampling.
	"""
	
	cran = "FossilSimShiny" 

	version("1.1.1", md5="bb2298c736e8ae5f204706dd20f14768")

	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-fossilsim", type=("build", "run"))
