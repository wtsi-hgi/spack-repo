# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcharts2shiny(RPackage):
	"""Embedding Interactive Charts Generated with ECharts Library into
Shiny Applications

	Embed interactive charts to their Shiny applications. These charts will be generated by ECharts library developed by Baidu (<http://echarts.baidu.com/>). Current version supports line chart, bar chart, pie chart, scatter plot, gauge, word cloud, radar chart, tree map, and heat map.
	"""
	
	homepage = "https://github.com/XD-DENG/ECharts2Shiny"
	cran = "ECharts2Shiny" 

	version("0.2.13", md5="2eb59e940337c1fc89f5954b366c6011")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
