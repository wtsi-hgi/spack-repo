# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinnts(RPackage):
	"""Microsoft Finance Time Series Forecasting Framework

	Automated time series forecasting developed by Microsoft Finance. The Microsoft Finance Time 
    Series Forecasting Framework, aka Finn, can be used to forecast any component of the income 
    statement, balance sheet, or any other area of interest by finance. Any numerical quantity over time, 
    Finn can be used to forecast it. While it can be applied outside of the finance domain, Finn was built 
    to meet the needs of financial analysts to better forecast their businesses within a company, and has 
    a lot of built in features that are specific to the needs of financial forecasters. Happy forecasting!
	"""
	
	homepage = "https://microsoft.github.io/finnts/"
	cran = "finnts" 

	version("0.4.0", md5="42b44fa93a364d607f7d1aa41096369e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-modeltime", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-cubist", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-feasts", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-hts", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-rules", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-timetk", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
