# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCon2lki(RPackage):
	"""Calculate the Dutch Air Quality Index (LKI)

	Calculates the dutch air quality index (LKI). This index was 
    created on the basis of scientific studies of the health effects of air 
    pollution. From these studies it can be deduced at what concentrations a 
    certain percentage of the population can be affected. For more information 
    see: <https://www.rivm.nl/bibliotheek/rapporten/2014-0050.pdf>.
	"""
	
	cran = "con2lki" 

	version("0.1.0", md5="bd162f7c55b701fb331b20b0802e492b")

