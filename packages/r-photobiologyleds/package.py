# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologyleds(RPackage):
	"""Spectral Data for Light-Emitting-Diodes

	Spectral emission data for some frequently used light emitting
    diodes available as electronic components. Part of the 'r4photobiology' 
    suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/photobiologyLEDs/"
	cran = "photobiologyLEDs" 

	version("0.5.2", md5="51cae7444c144d6f8f601f773a276e7d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.10.14:", type=("build", "run"))
