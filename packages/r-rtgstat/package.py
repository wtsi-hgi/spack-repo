# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtgstat(RPackage):
	"""Client for 'TGStat API'

	Allow function for using 'TGStat Stat API' and
    'TGStat Search API', for more details see <https://api.tgstat.ru/docs/ru/start/intro.html>.
    'TGStat' provide telegram channel analytics data.
	"""
	
	homepage = "https://selesnow.github.io/rtgstat/"
	cran = "rtgstat" 

	version("0.3.2", md5="f10b7611e444f34b1b241370bfa97ec5")

	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httr2@0.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
