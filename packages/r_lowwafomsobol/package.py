# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowwafomsobol(RPackage):
	"""Low WAFOM Sobol Sequence

	Implementation of Low Walsh Figure of Merit (WAFOM) sequence
        based on Sobol sequence.
	"""
	
	homepage = "https://mersennetwister-lab.github.io/LowWAFOMSobol/"
	cran = "LowWAFOMSobol" 

	version("1.1.1", md5="631d2f941ee017865a13c10ecaa39f66")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rsqlite@2:", type=("build", "run"))
