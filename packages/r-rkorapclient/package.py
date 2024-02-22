# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkorapclient(RPackage):
	"""'KorAP' Web Service Client Package

	A client package that makes the 'KorAP' web service API accessible from R.
  The corpus analysis platform 'KorAP' has been developed as a scientific tool to make
  potentially large, stratified and multiply annotated corpora, such as the 'German Reference Corpus DeReKo'
  or the 'Corpus of the Contemporary Romanian Language CoRoLa', accessible for linguists to let them verify
  hypotheses and to find interesting patterns in real language use.
  The 'RKorAPClient' package provides access to 'KorAP' and the corpora behind it for user-created R code,
  as a programmatic alternative to the 'KorAP' web user-interface.
  You can learn more about 'KorAP' and use it directly on 'DeReKo' at <https://korap.ids-mannheim.de/>.
	"""
	
	homepage = "https://github.com/KorAP/RKorAPClient/"
	cran = "RKorAPClient" 

	version("0.8.0", md5="916713315adf7b6a8c8449280f75a37c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-ptxqc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
