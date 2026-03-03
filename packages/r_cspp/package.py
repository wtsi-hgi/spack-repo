# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCspp(RPackage):
	"""A Tool for the Correlates of State Policy Project Data

	A tool that imports, subsets, visualizes, and exports the Correlates of State Policy Project dataset assembled by Marty P. Jordan and Matt Grossmann (2020) <http://ippsr.msu.edu/public-policy/correlates-state-policy>. The Correlates data contains over 2000 variables across more than 100 years that pertain to state politics and policy in the United States. Users with only a basic understanding of R can subset this data across multiple dimensions, export their search results, create map visualizations, export the citations associated with their searches, and more.
	"""
	
	cran = "cspp" 

	version("0.3.3", md5="3dead19cb3e2cbf178473589865600f6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-csppdata", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
