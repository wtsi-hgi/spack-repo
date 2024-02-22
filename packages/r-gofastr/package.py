# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofastr(RPackage):
	"""Fast DocumentTermMatrix and TermDocumentMatrix Creation

	Harness the power of 'quanteda', 'data.table' & 'stringi' to quickly generate 'tm' DocumentTermMatrix
             and TermDocumentMatrix data structures.
	"""
	
	homepage = "http://github.com/trinker/gofastr"
	cran = "gofastr" 

	version("0.3.0", md5="4b179f696b161d26a501dbf96fdc7eb3")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.5:", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
