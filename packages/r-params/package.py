# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParams(RPackage):
	"""Simplify Parameters

	An interface to simplify organizing parameters used in a package,
    using external configuration files. This attempts to provide a cleaner
    alternative to options().
	"""
	
	homepage = "https://github.com/sahilseth/params"
	cran = "params" 

	version("0.7.3", md5="4e46dbc413d9c820acb9560b7f7fdd09")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-rcpptoml", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
