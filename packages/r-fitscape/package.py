# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitscape(RPackage):
	"""Classes for Fitness Landscapes and Seascapes

	Convenient classes to model fitness landscapes and fitness
    seascapes. A low-level package with which most users will not interact but
    upon which other packages modeling fitness landscapes and fitness seascapes
    will depend.
	"""
	
	homepage = "https://github.com/rrrlw/fitscape"
	cran = "fitscape" 

	version("0.1.0", md5="f3d017a78362eedcab44cf134348743f")

