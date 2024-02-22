# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxkcd(RPackage):
	"""Get XKCD Comic from R

	Visualize your favorite XKCD comic strip directly from
        R. XKCD <https://xkcd.com> web comic content is provided under the Creative
        Commons Attribution-NonCommercial 2.5 License.
	"""
	
	cran = "RXKCD" 

	version("1.9.2", md5="15ed42616e88198ad9d6e02bdc4e8cb3")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
