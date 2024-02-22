# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUrootab(RPackage):
	"""Tabular Reporting of 'EViews' Unit Root Tests

	Conduct unit root tests based on 'EViews' (<https://eviews.com>) routines and report them in tables. 'EViews' (Econometric Views) is a commercial software for econometrics.
	"""
	
	homepage = "https://github.com/sagirumati/URooTab"
	cran = "URooTab" 

	version("0.1.0", md5="ba30d9d973d430b19b95957830154b11")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-eviewsr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
