# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetr(RPackage):
	"""Tools for Easier Analysis of Meteorological Fields

	Many useful functions and extensions for dealing
    with meteorological data in the tidy data framework. Extends 'ggplot2'
    for better plotting of scalar and vector fields and provides commonly
    used analysis methods in the atmospheric sciences.
	"""
	
	homepage = "https://eliocamp.github.io/metR/"
	cran = "metR" 

	version("0.15.0", md5="290d04139ae420099542606da5aff873")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
