# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDqastats(RPackage):
	"""Core Functions for Data Quality Assessment

	Perform data quality assessment ('DQA') of electronic health
    records ('EHR'). Publication: Kapsner et al. (2021)
    <doi:10.1055/s-0041-1733847>.
	"""
	
	homepage = "https://github.com/miracum/dqa-dqastats"
	cran = "DQAstats" 

	version("0.3.3", md5="3afbf0f053409bd67ec19e55ce727783")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-diztools@0.0.8:", type=("build", "run"))
	depends_on("r-dizutils@0.1.2:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-tinytex", type=("build", "run"))
