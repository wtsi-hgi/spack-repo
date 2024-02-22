# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAttachment(RPackage):
	"""Deal with Dependencies

	Manage dependencies during package development. This can
    retrieve all dependencies that are used in ".R" files in the "R/"
    directory, in ".Rmd" files in "vignettes/" directory and in 'roxygen2'
    documentation of functions. There is a function to update the
    "DESCRIPTION" file of your package with 'CRAN' packages or any other
    remote package.  All functions to retrieve dependencies of ".R"
    scripts and ".Rmd" or ".qmd" files can be used independently of a
    package development.
	"""
	
	homepage = "https://thinkr-open.github.io/attachment/"
	cran = "attachment" 

	version("0.4.1", md5="2673bccd0aa68cc0a7abe8058444d3fd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc@1.2:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rmarkdown@1.10:", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
