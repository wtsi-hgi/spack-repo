# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqti(RPackage):
	"""Create Tests According to QTI 2.1 Standard

	Create tests and tasks compliant with the Question & Test Interoperability (QTI) information model version 2.1. Input sources are Rmd/md description files or S4-class objects. Output formats include standalone zip or xml files. Supports the generation of basic task types (single and multiple choice, order, pair association, matching tables, filling gaps and essay) and provides a comprehensive set of attributes for customizing tests.
	"""
	
	homepage = "https://github.com/shevandrin/rqti"
	cran = "rqti" 

	version("0.1.1", md5="7db2f8da623a1ba6d29b9f0b5f2f6778")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
