# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REiopar(RPackage):
	"""Access to RFR (Risk-Free Rate) Curves Produced by the EIOPA

	Provides EIOPA (European Insurance And Occupational Pensions Authority) risk-free rates. Please note that the author of this package is not affiliated with EIOPA. The data is accessed through a REST API available at <https://mehdiechchelh.com/api/>.
	"""
	
	cran = "eiopaR" 

	version("0.1.1", md5="d680f248a789d9114c28c8de6c516645")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
