# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRalsa(RPackage):
	"""R Analyzer for Large-Scale Assessments

	
    Prepare and analyze data from large-scale assessments and surveys with
    complex sampling and assessment design (see 'Rutkowski', 2010
    <doi:10.3102/0013189X10363170>). Such studies are, for example,
    international assessments like 'TIMSS', 'PIRLS' and 'PISA'. A graphical
    interface is available for the non-technical user.The package includes
    functions to covert the original data from 'SPSS' into 'R' data sets
    keeping the user-defined missing values, merge data from different
    respondents and/or countries, generate variable dictionaries, modify
    data, produce descriptive statistics (percentages, means, percentiles,
    benchmarks) and multivariate statistics (correlations, linear
    regression, binary logistic regression). The number of supported
    studies and analysis types will increase in future. For a general
    presentation of the package, see 'Mirazchiyski', 2021a
    (<doi:10.1186/s40536-021-00114-4>). For detailed technical aspects of the
    package, see 'Mirazchiyski', 2021b (<doi:10.3390/psych3020018>).
	"""
	
	homepage = "https://ralsa.ineri.org/"
	cran = "RALSA" 

	version("1.4.0", md5="e7a202bcde49dcecda62b1995ee8d63b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-import", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rclipboard", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
