# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorldfootballr(RPackage):
	"""Extract and Clean World Football (Soccer) Data

	Allow users to obtain clean and tidy
    football (soccer) game, team and player data. Data is collected from a
    number of popular sites, including 'FBref',
    transfer and valuations data from
    'Transfermarkt'<https://www.transfermarkt.com/> and shooting location
    and other match stats data from 'Understat'<https://understat.com/>
    and 'fotmob'<https://www.fotmob.com/>. It gives users the
    ability to access data more efficiently, rather than having to export
    data tables to files before being able to complete their analysis.
	"""
	
	homepage = "https://github.com/JaseZiv/worldfootballR"
	cran = "worldfootballR" 

	version("0.6.2", md5="be3dffaee5c9fff96d876b1d1be8cf84")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
