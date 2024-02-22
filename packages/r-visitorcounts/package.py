# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisitorcounts(RPackage):
	"""Modeling and Forecasting Visitor Counts Using Social Media

	Performs modeling and forecasting of park visitor counts
	using social media data and (partial) on-site visitor counts.
	Specifically, the model is built based on an automatic decomposition
	of the trend and seasonal components of the social media-based park visitor counts,
	from which short-term forecasts of the visitor counts and percent changes
	in the visitor counts can be made. A reference for generating social media-based
	visitor counts can be found at
	Wood, Guerry, Silver, and Lacayo (2013) <doi:10.1038/srep02976>.
	"""
	
	cran = "VisitorCounts" 

	version("1.0.2", md5="a60965d3b3ad03ff678dd54781a6c51b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rssa", type=("build", "run"))
