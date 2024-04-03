# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemisc(RPackage):
	"""Management of Survey Data and Presentation of Analysis Results.

	An infrastructure for the management of survey data including value labels,
	definable missing values, recoding of variables, production of code books,
	and import of (subsets of) 'SPSS' and 'Stata' files is provided. Further,
	the package allows to produce tables and data frames of arbitrary
	descriptive statistics and (almost) publication-ready tables of regression
	model estimates, which can be exported to 'LaTeX' and HTML."""

	cran = "memisc"
	version("0.99.31.6", sha256="52336b4ffc6e60c3ed10ccc7417231582b0d2e4c5c3b2184396a7d3ca9c1d96e")
	version("0.99.31.7", md5="29549169c78c37545bb79bb7ac4753c9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
