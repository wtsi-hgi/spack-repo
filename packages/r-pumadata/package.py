# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPumadata(RPackage):
	"""Various data sets for use with the puma package

	This is a simple data package including various data sets derived from the estrogen data for use with the puma (Propagating Uncertainty in Microarray Analysis) package.
	"""
	
	homepage = "http://umber.sbs.man.ac.uk/resources/puma"
	bioc = "pumadata"

	version("2.44.0", commit="5c3b82f20e579b75100404b148738ad4199ed6a7")
	version("2.38.0", commit="da7fe7e5fd40b6fe1248d242c1cd21838feceae6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-puma", type=("build", "run"))
	depends_on("r-oligo@1.32:", type=("build", "run"))

