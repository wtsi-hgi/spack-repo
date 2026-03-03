# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHlidacr(RPackage):
	"""Access Data from the 'Hlídač Státu' API

	Provides access to datasets published by 'Hlídač státu' <https://www.hlidacstatu.cz/>, 
    a Czech watchdog, via their API. 
	"""
	
	homepage = "https://github.com/skvrnami/hlidacr"
	cran = "hlidacr" 

	version("0.2.0", md5="1990d425cffe5ad35198b5cc8eb696e0")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
