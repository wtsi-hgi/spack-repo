# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologyplants(RPackage):
	"""Plant Photobiology Related Functions and Data

	Provides functions for quantifying visible (VIS) and ultraviolet
    (UV) radiation in relation to the photoreceptors Phytochromes,
    Cryptochromes, and UVR8 which are present in plants. It also includes data 
    sets on the optical properties of plants. Part of the 'r4photobiology' 
    suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/photobiologyPlants/"
	cran = "photobiologyPlants" 

	version("0.5.0", md5="45a3a7d0cc26a5a69dfbb9e153872d03")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.11.2:", type=("build", "run"))
	depends_on("r-photobiologywavebands@0.5.2:", type=("build", "run"))
