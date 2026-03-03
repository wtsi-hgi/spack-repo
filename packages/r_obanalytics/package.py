# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObanalytics(RPackage):
	"""Limit Order Book Analytics

	Data processing, visualisation and analysis of Limit Order Book
    event data.
	"""
	
	homepage = "https://github.com/phil8192/ob-analytics"
	cran = "obAnalytics" 

	version("0.1.1", md5="7f9272ec14108139165446c6ab62cdca")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
