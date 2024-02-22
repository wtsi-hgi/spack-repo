# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpn(RPackage):
	"""Most Probable Number and Other Microbial Enumeration Techniques

	Calculates the Most Probable Number (MPN) to quantify the
    concentration (density) of microbes in serial dilutions of a laboratory
    sample (described in Jarvis, 2010 <doi:10.1111/j.1365-2672.2010.04792.x>).
    Also calculates the Aerobic Plate Count (APC) for similar microbial
    enumeration experiments.
	"""
	
	homepage = "https://mpncalc.galaxytrakr.org/"
	cran = "MPN" 

	version("0.3.0", md5="a9dfaefd74a9058af99e5738eeffe050")

	depends_on("r@3.4:", type=("build", "run"))
