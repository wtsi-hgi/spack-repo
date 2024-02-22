# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidypaleo(RPackage):
	"""Tidy Tools for Paleoenvironmental Archives

	Provides a set of functions with a common framework for age-depth model management, 
  stratigraphic visualization, and common statistical transformations. The focus of the
  package is stratigraphic visualization, for which 'ggplot2' components are provided
  to reproduce the scales, geometries, facets, and theme elements commonly used in
  publication-quality stratigraphic diagrams. Helpers are also provided to reproduce
  the exploratory statistical summaries that are frequently included on
  stratigraphic diagrams. See Dunnington et al. (2021) <doi:10.18637/jss.v101.i07>.
	"""
	
	homepage = "https://paleolimbot.github.io/tidypaleo/"
	cran = "tidypaleo" 

	version("0.1.3", md5="d074ed7915b4e7bdb8d4a4de91b12b86")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-styler", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rioja", type=("build", "run"))
