# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolileucine(RPackage):
	"""Experimental data with Affymetrix E. coli chips

	Experimental data with Affymetrix E. coli chips, as reported in She-pin Hung, Pierre Baldi, and G. Wesley Hatfield, J. Biol. Chem., Vol. 277, Issue 43, 40309-40323, October 25, 2002
	"""
	
	bioc = "ecoliLeucine"

	version("1.48.0", commit="af25ebe7503bd3f5ee7d528d9f7570571f3e1d2b")
	version("1.42.0", commit="d3789b4af6a65a28da2ae0cfa97408660547aca7")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-ecolicdf", type=("build", "run"))

