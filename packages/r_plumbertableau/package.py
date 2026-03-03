# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlumbertableau(RPackage):
	"""Turn 'Plumber' APIs into 'Tableau' Extensions

	Build 'Plumber' APIs that can be used in 'Tableau' workbooks.
    Annotations in R comments allow APIs to conform to the 'Tableau Analytics
    Extension' specification, so that R code can be used to power 'Tableau'
    workbooks.
	"""
	
	homepage = "https://rstudio.github.io/plumbertableau/"
	cran = "plumbertableau" 

	version("0.1.1", md5="c55eb61301bbf871b0e89d43da397362")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plumber@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-debugme", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
