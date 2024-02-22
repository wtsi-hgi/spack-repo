# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsv(RPackage):
	"""Read and Write CSV Files with Selected Conventions

	Reads and writes CSV with selected conventions.
 Uses the same generic function for reading and writing to promote consistent formats.
	"""
	
	cran = "csv" 

	version("0.6.2", md5="36091bca25685e0deb2b9adcd30b4bba")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
