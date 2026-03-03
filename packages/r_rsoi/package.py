# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsoi(RPackage):
	"""Import Various Northern and Southern Hemisphere Climate Indices

	Downloads Southern Oscillation Index, Oceanic Nino
    Index, North Pacific Gyre Oscillation data, North Atlantic Oscillation
    and Arctic Oscillation. Data sources are described in the help files for each function.
	"""
	
	homepage = "https://github.com/boshek/rsoi/"
	cran = "rsoi" 

	version("0.5.6", md5="50f17fead0b6fcd49328dc1fe7bb1152")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
