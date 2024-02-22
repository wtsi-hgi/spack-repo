# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeozoo(RPackage):
	"""Zoo of Geometric Objects

	Geometric objects defined in 'geozoo' can be simulated or displayed in the R package 'tourr'.
	"""
	
	homepage = "http://schloerke.github.io/geozoo/"
	cran = "geozoo" 

	version("0.5.1", md5="81b83e5a45a7c9195634b7fa31a578d4")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
