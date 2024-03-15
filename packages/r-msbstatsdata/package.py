# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbstatsdata(RPackage):
	"""Data Sets for Courses at the Münster School of Business

	Provides sample data sets that are used in statistics and data science courses at the Münster School of Business. The datasets refer to different business topics but also other domains, e.g. sports, traffic, etc.
	"""
	
	cran = "MSBStatsData" 

	version("0.0.2", md5="45e14311fc86c558cef26a50c13e034b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
