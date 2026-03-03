# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdicdata(RPackage):
	"""Accessing FDIC Bank Data

	A system provides a set of functions for
    working with data from the Federal Deposit Insurance Corporation
    (FDIC), including retrieving financial data for FDIC-insured
    institutions and accessing the data taxonomy.
	"""
	
	homepage = "https://github.com/visbanking/fdicdata"
	cran = "fdicdata" 

	version("0.1.0", md5="6454783407e25da6bd53709ac7cc0b17")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
