# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistdata(RPackage):
	"""Data Sets from the History of Statistics and Data Visualization

	The 'HistData' package provides a collection of small data sets
    that are interesting and important in the history of statistics and data
    visualization. The goal of the package is to make these available, both for
    instructional use and for historical research. Some of these present interesting
    challenges for graphics or analysis in R.
	"""
	
	homepage = "https://friendly.github.io/HistData/"
	cran = "HistData" 

	version("0.9-1", md5="2a9d0f8478c1d276d95b986a3326b391")

	depends_on("r@3.5:", type=("build", "run"))
