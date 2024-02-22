# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgeoX(RPackage):
	"""Access Small ForestGEO Datasets For Examples

	Access small example datasets from Luquillo, a
    ForestGEO site in Puerto Rico
    (<https://forestgeo.si.edu/sites/north-america/luquillo>).
	"""
	
	homepage = "https://github.com/forestgeo/fgeo.x"
	cran = "fgeo.x" 

	version("1.1.4", md5="d5e911ede11ce9b935be13a63ef67470")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-memoise@1.1:", type=("build", "run"))
