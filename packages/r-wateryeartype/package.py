# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWateryeartype(RPackage):
	"""Sacramento and San Joaquin Valley Water Year Types

	Provides Water Year Hydrologic Classification Indices based on measured 
    unimpaired runoff (in million acre-feet). Data is provided by California Department of Water Resources
    and subject to revision.
	"""
	
	cran = "waterYearType" 

	version("1.0.1", md5="56a80c2b1f1497214285caba2fba2304")

	depends_on("r@2.10:", type=("build", "run"))
