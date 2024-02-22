# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBelex(RPackage):
	"""Download Historical Data from the Belgrade Stock Exchange

	Tools for downloading historical financial data from the www.belex.rs.
	"""
	
	cran = "belex" 

	version("0.1.0", md5="dd1f73d745ab4c85eda679bef4d64157")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
