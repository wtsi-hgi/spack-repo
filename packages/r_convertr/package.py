# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvertr(RPackage):
	"""Convert Between Units

	Provides conversion functionality between a broad range of
    scientific, historical, and industrial unit types.
	"""
	
	cran = "convertr" 

	version("0.1", md5="86a47553a89ca2644e3a771d3533d248")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-shiny@0.13.2:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-dt@0.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
