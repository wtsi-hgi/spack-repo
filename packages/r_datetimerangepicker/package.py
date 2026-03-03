# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatetimerangepicker(RPackage):
	"""A Datetime Range Picker Widget for Usage in 'Shiny' Applications

	Provides a datetime range picker widget for usage in 'Shiny'.
    It creates a calendar allowing to select a start date and an end date
    as well as two fields allowing to select a start time and an end time.
	"""
	
	homepage = "https://github.com/stla/DateTimeRangePicker"
	cran = "DateTimeRangePicker" 

	version("1.1.0", md5="5f56d3bf0549a69335694cdd5f6d2a29")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
