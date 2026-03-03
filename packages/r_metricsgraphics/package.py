# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetricsgraphics(RPackage):
	"""Create Interactive Charts with the JavaScript 'MetricsGraphics'
Library

	Provides an 'htmlwidgets' interface to the
    'MetricsGraphics.js' ('D3'-based) charting library which is geared towards
    displaying time-series data. Chart types include line charts, scatterplots,
    histograms and rudimentary bar charts. Support for laying out multiple charts
    into a grid layout is also provided. All charts are interactive and many
    have an option for line, label and region annotations.
	"""
	
	homepage = "http://github.com/hrbrmstr/metricsgraphics"
	cran = "metricsgraphics" 

	version("0.9.0", md5="2053e6bd40b0d0f73c602c54bf37a726")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
