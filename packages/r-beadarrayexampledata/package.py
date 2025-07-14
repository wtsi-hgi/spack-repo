# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadarrayexampledata(RPackage):
	"""Example data for the beadarray package

	An small dataset that can be used to run examples from the beadarray vignette and examples
	"""
	
	bioc = "beadarrayExampleData"

	version("1.46.0", commit="2eda6493838b25af3366a200a9b1ae65f8e9babd")
	version("1.40.0", commit="b19df3c2deebd5622a7ecb3df9a4b81437f639da")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-beadarray@2:", type=("build", "run"))

