# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTangram(RPackage):
	"""The Grammar of Tables

	Provides an extensible formula system to quickly and easily create
    production quality tables. The processing steps are a formula parser,
    statistical content generation from data as defined by formula, followed by
    rendering into a table. Each step of the processing is separate and user
    definable thus creating a set of composable building blocks for
    highly customizable table generation. A user is not limited by any of the 
    choices of the package creator other than the formula grammar. For example,
    one could chose to add a different S3 rendering function and output a format
    not provided in the default package, or possibly one would rather have Gini
    coefficients for their statistical content in a resulting table. Routines to
    achieve New England Journal of Medicine style, Lancet style and
    Hmisc::summaryM() statistics are provided. The package contains rendering
    for HTML5, Rmarkdown and an indexing format for use in tracing and tracking
    are provided.
	"""
	
	homepage = "https://github.com/spgarbet/tangram"
	cran = "tangram" 

	version("0.8.2", md5="f5171bf25b5595771a3faba1b2f527c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
