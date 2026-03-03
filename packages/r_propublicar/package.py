# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPropublicar(RPackage):
	"""Access Functions for ProPublica's APIs

	Provides wrapper functions to access the ProPublica's Congress and Campaign Finance APIs.
    The Congress API provides near real-time access to legislative data from the House of 
    Representatives, the Senate and the Library of Congress.
    The Campaign Finance API provides data from United States Federal Election Commission 
    filings and other sources. The API covers summary information for candidates and 
    committees, as well as certain types of itemized data.
    For more information about these APIs go to: <https://www.propublica.org/datastore/apis>.
	"""
	
	cran = "ProPublicaR" 

	version("1.1.4", md5="cfff91c745b1b0c90089202ba733563f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
