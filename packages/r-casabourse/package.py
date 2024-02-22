# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasabourse(RPackage):
	"""Casablanca Stock Exchange Data

	It provides real-time data from the Casablanca Stock Exchange. The objective is to facilitate access to data for all users of the R programming language. 
             It includes a variety of data accessible just by function call.
	"""
	
	homepage = "https://github.com/AODiakite"
	cran = "casabourse" 

	version("2.0.0", md5="5991110e3ffe135bcfe88d17ab99453e")

	depends_on("r-gsheet", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
