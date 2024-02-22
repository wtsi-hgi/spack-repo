# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFtdk(RPackage):
	"""A Wrapper for the API of the Danish Parliament

	A wrapper for the API of the Danish Parliament. It makes it 
    possible to get data from the API easily into a data frame. Learn more at 
    <http://www.ft.dk/dokumenter/aabne_data>.
	"""
	
	homepage = "https://github.com/mikkelkrogsholm/ftDK"
	cran = "ftDK" 

	version("1.0", md5="ed77d863b117a4ac2a1b5d5952795b2a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
