# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaterangepicker(RPackage):
	"""Create a Shiny Date-Range Input

	A Shiny Input for date-ranges, which pops up two calendars for selecting dates, times, or predefined ranges like "Last 30 Days". It wraps the JavaScript library 'daterangepicker' which is available at <https://www.daterangepicker.com>.
	"""
	
	homepage = "https://github.com/trafficonese/daterangepicker/"
	cran = "daterangepicker" 

	version("0.2.0", md5="523d3b30c99a060e89119f454fddbd8f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonify", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
