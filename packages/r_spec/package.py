# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpec(RPackage):
	"""A Data Specification Format and Interface

	Creates a data specification that describes the columns of a 
 table (data.frame). Provides methods to read, write, and update the 
 specification. Checks whether a table matches its specification. See
 specification.data.frame(),read.spec(), write.spec(), as.csv.spec(),
 respecify.character(), and %matches%.data.frame().
	"""
	
	cran = "spec" 

	version("0.1.9", md5="8256cd8e4cf8754c874f5bbcce2cc4f4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-encode", type=("build", "run"))
	depends_on("r-csv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
