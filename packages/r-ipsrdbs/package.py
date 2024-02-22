# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpsrdbs(RPackage):
	"""Introduction to Probability, Statistics and R for Data Based
Sciences

	Contains data sets, programmes and illustrations 
    discussed in the book, "Introduction to Probability, Statistics and R:
    Foundations for Data-Based Sciences."  Sahu (2023, isbn:978-3-031-37864-5)
    describes the methods in detail.
	"""
	
	homepage = "https://www.sujitsahu.com"
	cran = "ipsRdbs" 

	version("0.2.6", md5="b88270cabdeba01f2b42c24bac3cae62")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
