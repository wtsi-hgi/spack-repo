# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebglobe(RPackage):
	"""3D Interactive Globes

	Displays geospatial data on an interactive 3D globe in the web browser.
	"""
	
	homepage = "https://github.com/r-barnes/webglobe/"
	cran = "webglobe" 

	version("1.0.3", md5="4f320618b1ce1104b28d4e0a55a7f168")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-geojsonio@0.3.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.4:", type=("build", "run"))
	depends_on("r-httpuv@1.3.3:", type=("build", "run"))
