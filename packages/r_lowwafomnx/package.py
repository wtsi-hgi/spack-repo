# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowwafomnx(RPackage):
	"""Low WAFOM Niederreiter-Xing Sequence

	Implementation of Low Walsh Figure of Merit (WAFOM) sequence
        based on Niederreiter-Xing sequence <DOI:10.1007/978-3-642-56046-0_30>.
	"""
	
	homepage = "https://mersennetwister-lab.github.io/LowWAFOMNX/"
	cran = "LowWAFOMNX" 

	version("1.1.1", md5="d397e647b0edef050f6eee72281f7144")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rsqlite@2:", type=("build", "run"))
