# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProverbs(RPackage):
	"""Print a Daily Bible Proverb to Console

	A simple package to grab a Bible proverb corresponding to the
    day of the month.
	"""
	
	homepage = "https://github.com/bradlindblad/proverbs"
	cran = "proverbs" 

	version("0.4.0", md5="43c7e563b3580b83bb0cf9002a626f1c")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
