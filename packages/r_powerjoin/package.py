# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerjoin(RPackage):
	"""Extensions of 'dplyr' and 'fuzzyjoin' Join Functions

	We extend 'dplyr' and 'fuzzyjoin' join functions with
    features to preprocess the data, apply various data checks, and deal with
    conflicting columns.
	"""
	
	homepage = "https://github.com/moodymudskipper/powerjoin"
	cran = "powerjoin" 

	version("0.1.0", md5="44439f410d14db4be03996b73e8dfaf0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
