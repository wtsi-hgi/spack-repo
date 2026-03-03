# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipangu(RPackage):
	"""Japanese Utility Functions and Data

	Some data treated by the Japanese R user require
    unique operations and processing. These are caused by address, Kanji,
    and traditional year representations. 'zipangu' transforms specific
    to Japan into something more general one.
	"""
	
	homepage = "https://uribo.github.io/zipangu/"
	cran = "zipangu" 

	version("0.3.2", md5="3cd9a551615f74bf512fbbf320053137")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-lifecycle@0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-stringi@1.4.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-arabic2kansuji@0.1:", type=("build", "run"))
