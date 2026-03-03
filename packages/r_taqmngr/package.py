# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaqmngr(RPackage):
	"""Manage Tick-by-Tick Transaction Data

	Manager of tick-by-tick transaction data that performs 'cleaning', 'aggregation' and 'import' in an efficient and fast way. The package engine, written in C++, exploits the 'zlib' and 'gzstream' libraries to handle gzipped data without need to uncompress them. 'Cleaning' and 'aggregation' are performed according to Brownlees and Gallo (2006) <DOI:10.1016/j.csda.2006.09.030>. Currently, TAQMNGR processes raw data from WRDS (Wharton Research Data Service, <https://wrds-web.wharton.upenn.edu/wrds/>).
	"""
	
	homepage = "https://cran.r-project.org/package=TAQMNGR"
	cran = "TAQMNGR" 

	version("2018.5-1", md5="ee4d46eb26fee96e79cffb530bcf4158")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
