# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNdtv(RPackage):
	"""Network Dynamic Temporal Visualizations

	Renders dynamic network data from 'networkDynamic' objects as movies, interactive animations, or other representations of changing relational structures and attributes.
	"""
	
	homepage = "https://github.com/statnet/ndtv"
	cran = "ndtv" 

	version("0.13.3", md5="75d0a56ab7f39dfb5a426fd901587028")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-network@1.13:", type=("build", "run"))
	depends_on("r-networkdynamic@0.9:", type=("build", "run"))
	depends_on("r-animation@2.4:", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-base64", type=("build", "run"))
