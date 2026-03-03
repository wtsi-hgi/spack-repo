# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRworldxtra(RPackage):
	"""Country boundaries at high resolution

	High resolution vector country boundaries derived from
        Natural Earth data, can be plotted in rworldmap.
	"""
	
	cran = "rworldxtra" 

	version("1.01", md5="400de59e2b5cde61faf5224db532d22e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
