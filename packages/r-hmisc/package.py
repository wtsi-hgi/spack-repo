# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmisc(RPackage):
	"""Harrell Miscellaneous.

	Contains many functions useful for data analysis, high-level graphics,
	utility operations, functions for computing sample size and power,
	importing and annotating datasets, imputing missing values, advanced table
	making, variable clustering, character string manipulation, conversion of R
	objects to LaTeX and html code, and recoding variables."""

	cran = "Hmisc"

	version("5.1-1", md5="5ec7c524fdea5b77eddcbdae3c368968")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmltable@1.11:", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
