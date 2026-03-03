# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastverse(RPackage):
	"""A Suite of High-Performance Packages for Statistics and Data
Manipulation

	Easy installation, loading and management, of high-performance packages 
             for statistical computing and data manipulation in R. 
             The core 'fastverse' consists of 4 packages: 'data.table', 'collapse', 
             'kit' and 'magrittr', that jointly only depend on 'Rcpp'. 
             The 'fastverse' can be freely and permanently extended with 
             additional packages, both globally or for individual projects. 
             Separate package verses can also be created. Fast packages 
             for many common tasks such as time series, dates and times, strings, 
             spatial data, statistics, data serialization, larger-than-memory 
             processing, and compilation of R code are listed in the README file: 
             <https://github.com/fastverse/fastverse#suggested-extensions>.
	"""
	
	homepage = "https://fastverse.github.io/fastverse/"
	cran = "fastverse" 

	version("0.3.2", md5="4170e928ae059f1a3a39547899d7379b")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-kit", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
