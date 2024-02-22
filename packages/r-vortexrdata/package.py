# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVortexrdata(RPackage):
	"""Example Data for R Package 'vortexR'

	Contains selected data from two publications,
    Campbell 'et' 'al'. (2016) <DOI:10.1080/14486563.2015.1028486>
    and 'Pacioni' 'et' 'al'. (2017) <DOI:10.1071/PC17002>.
    The data is provided both as raw outputs from the population viability
    analysis software 'Vortex' and packaged as R objects.
    The R package 'vortexR' uses the raw data provided here to illustrate its
    functionality of parsing raw 'Vortex' output into R objects.
	"""
	
	homepage = "https://github.com/carlopacioni/vortexRdata/"
	cran = "vortexRdata" 

	version("1.0.5", md5="04e04404c728c3f5fb0209810522071c")

	depends_on("r@3.1:", type=("build", "run"))
