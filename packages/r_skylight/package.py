# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkylight(RPackage):
	"""A Simple Sky Illuminance Model

	A tool to calculate sky illuminance values (in lux) for both sun and moon. The
 model is a verbatim translation of the code by Janiczek and DeYoung (1987)
 <https://archive.org/details/DTIC_ADA182110>.
	"""
	
	homepage = "https://github.com/bluegreen-labs/skylight"
	cran = "skylight" 

	version("1.2", md5="f65d184f227ff90b5ce3a35b85be9651")

	depends_on("r@3.6:", type=("build", "run"))
