# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaqcsubset(RPackage):
	"""Experimental Data Package: MAQCsubset

	Data Package automatically created on Sun Nov 19 15:59:29 2006.
	"""
	
	bioc = "MAQCsubset"

	version("1.46.0", commit="37fdb74cd9b910536e2df13dba8e8293dbf2b01e")
	version("1.40.0", commit="708a5e938ec03cad83241a6d6bf2d07ec1287fcd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

