# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvdebugr(RPackage):
	"""A Time-Travelling Debugger

	Uses provenance post-execution to help the user understand
    and debug their script by providing functions to look at intermediate steps and
    data values, their forwards and backwards lineage, and to understand the
    steps leading up to warning and error messages. 'provDebugR' uses
    provenance produced by 'rdtLite' (available on CRAN), stored in PROV-JSON format.
	"""
	
	cran = "provDebugR" 

	version("1.0.1", md5="cef27d4b0dc60f61f464b291b98d2526")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-provgraphr", type=("build", "run"))
	depends_on("r-provparser", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
