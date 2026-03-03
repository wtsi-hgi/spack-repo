# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapsfinland(RPackage):
	"""Maps of Finland

	Maps and other related data of Finland.
	"""
	
	cran = "mapsFinland" 

	version("0.2.2", md5="7effaa09aad9c1186b49692645215977")

	depends_on("r@3.5:", type=("build", "run"))
