# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdbnomics(RPackage):
	"""Download DBnomics Data

	R access to hundreds of millions data series from DBnomics API
    (<https://db.nomics.world/>).
	"""
	
	homepage = "https://git.nomics.world/dbnomics/rdbnomics"
	cran = "rdbnomics" 

	version("0.6.4", md5="4edde010e31704724eeb9afb27d5b178")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
