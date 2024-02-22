# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNflverse(RPackage):
	"""Easily Install and Load the 'nflverse'

	The 'nflverse' is a set of packages dedicated to data of the
    National Football League. This package is designed to make it easy to
    install and load multiple 'nflverse' packages in a single step. Learn
    more about the 'nflverse' at <https://nflverse.nflverse.com/>.
	"""
	
	homepage = "https://nflverse.nflverse.com/"
	cran = "nflverse" 

	version("1.0.3", md5="889602c5d8ca1ef2425a204357837fe6")

	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-crayon@1.4:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-nfl4th@1.0.3:", type=("build", "run"))
	depends_on("r-nflfastr@4.5.1:", type=("build", "run"))
	depends_on("r-nflplotr@1.1:", type=("build", "run"))
	depends_on("r-nflreadr@1.3.2:", type=("build", "run"))
	depends_on("r-nflseedr@1.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
