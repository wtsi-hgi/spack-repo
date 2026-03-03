# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatareporter(RPackage):
	"""Reproducible Data Screening Checks and Report of Possible Errors

	Data screening is an important first step of any statistical
    analysis. 'dataReporter' auto generates a customizable data report with a thorough
    summary of the checks and the results that a human can use to identify possible
    errors. It provides an extendable suite of test for common potential
    errors in a dataset. See Petersen AH, Ekstrøm CT (2019). "dataMaid: Your Assistant for Documenting Supervised Data Quality Screening in R." _Journal of Statistical Software_, *90*(6), 1-38 <doi:10.18637/jss.v090.i06> for more information.
	"""
	
	homepage = "https://github.com/ekstroem/dataReporter"
	cran = "dataReporter" 

	version("1.0.2", md5="0743d84c468c9e16a24f01b209d0147e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-rmarkdown@1.10:", type=("build", "run"))
	depends_on("r-robustbase@0.93.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-whoami", type=("build", "run"))
	depends_on("pandoc@2.0:", type=("build", "link", "run"))
	depends_on("git", type=("build", "link", "run"))
