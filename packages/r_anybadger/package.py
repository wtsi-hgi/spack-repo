# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnybadger(RPackage):
	"""Create Custom Pipeline Badges

	
    You can use this package to create custom pipeline badges in a standard 'svg' format.
    This is useful for a company to use internally, where it may not be possible
    to create badges through external providers.
    This project was inspired by the 'anybadge' library in python.
	"""
	
	homepage = "https://github.com/lmeninato/anybadger"
	cran = "anybadger" 

	version("0.1.0", md5="dbbd556d71ebe0b88a8dd1593a74de7a")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
