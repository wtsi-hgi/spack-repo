# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRitch(RPackage):
	"""R Parser for the ITCH-Protocol

	Allows to efficiently parse, filter, and write binary ITCH Files (Version 5.0) containing detailed financial transactions as distributed by NASDAQ to an R data.table.
	"""
	
	homepage = "https://davzim.github.io/RITCH/"
	cran = "RITCH" 

	version("0.1.26", md5="f0be4925964447712c63b3dbe4697171")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nanotime@0.3.2:", type=("build", "run"))
	depends_on("r-bit64@4.0.5:", type=("build", "run"))
