# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyebiasexamples(RPackage):
	"""Example data for the dyebias package, which implements the GASSCO method.

	Data for the dyebias package, consisting of 4 self-self hybrizations of self-spotted yeast slides, as well as data from Array Express accession E-MTAB-32
	"""
	
	homepage = "http://www.holstegelab.nl/publications/margaritis_lijnzaad"
	bioc = "dyebiasexamples"

	version("1.48.0", commit="4661605f7c7d3fe5e0717f2dfc79c87fc7e37ba2")
	version("1.42.0", commit="9929f423be5706a9e86a2d9ee920be2b519afd90")

	depends_on("r@1.4.1:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

