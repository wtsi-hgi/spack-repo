# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlattabler(RPackage):
	"""Obtaining a Flat Table from Pivot Tables

	Transformations that allow obtaining a flat table from
    reports in text or Excel format that contain data in the form of pivot
    tables. They can be defined for a single report and applied to a set
    of reports.
	"""
	
	homepage = "https://josesamos.github.io/flattabler/"
	cran = "flattabler" 

	version("2.1.1", md5="ae57184227cb485fa33c0be264206dde")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
