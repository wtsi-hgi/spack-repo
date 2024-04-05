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
	in the visitor counts can be made. A reference for the underlying model that 'VisitorCounts' uses can be found at 
    'Russell Goebel', Austin Schmaltz, 'Beth Ann Brackett', Spencer A. Wood, 'Kimihiro Noguchi' (2023) <doi:10.1002/for.2965> .
	"""
	
	cran = "VisitorCounts" 

	version("2.0.0", md5="81d7a2a3ce5d376e6729288613d8d17e")
	version("1.0.2", md5="a60965d3b3ad03ff678dd54781a6c51b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rssa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
