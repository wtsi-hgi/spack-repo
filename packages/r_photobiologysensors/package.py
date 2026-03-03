# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologysensors(RPackage):
	"""Response Data for Light Sensors

	Spectral response data for broadband ultraviolet and visible
    radiation sensors. Angular response data for broadband ultraviolet and visible
    radiation sensors and diffusers used as entrance optics. Data obtained from
    multiple sources were used: author-supplied data from scientific research 
    papers, sensor-manufacturer supplied data, and published sensor 
    specifications. Part of the 'r4photobiology' suite Aphalo P. J. (2015) 
    <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://www.r4photobiology.info"
	cran = "photobiologySensors" 

	version("0.5.1", md5="2f0e8994632767b5bcd0652dd85e846a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.11:", type=("build", "run"))
