# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM5(RPackage):
	"""'M5 Forecasting' Challenges Data

	Contains functions, which facilitate downloading, loading and preparing data from 'M5 Forecasting' challenges (by 'University of Nicosia', hosted on 'Kaggle'). 
  The data itself is set of time series of different product sales in 'Walmart'.
  The package also includes a ready-to-use built-in M5 subset named 'tiny_m5'.
  For detailed information about the challenges, see:
  Makridakis, S. & Spiliotis, E. & Assimakopoulos, V. (2020). <doi:10.1016/j.ijforecast.2021.10.009>.
	"""
	
	homepage = "https://github.com/krzjoa/m5"
	cran = "m5" 

	version("0.1.1", md5="112390df8c2e85f2841993cc65fe61c6", url="https://cran.r-project.org/src/contrib/m5_0.1.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
