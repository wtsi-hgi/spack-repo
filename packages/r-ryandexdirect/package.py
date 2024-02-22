# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRyandexdirect(RPackage):
	"""Load Data From 'Yandex Direct'

	Load data from 'Yandex Direct' API V5 
    <https://yandex.ru/dev/direct/doc/dg/concepts/about-docpage> into R.
	Provide function for load lists of campaings, ads, keywords and other 
	objects from 'Yandex Direct' account. Also you can load statistic from
	API 'Reports Service' <https://yandex.ru/dev/direct/doc/reports/reports-docpage>.
	And allows keyword bids management.
	"""
	
	homepage = "https://selesnow.github.io/ryandexdirect/"
	cran = "ryandexdirect" 

	version("3.6.2", md5="526211b2665cb65c64180ad325da5ce1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
