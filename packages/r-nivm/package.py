# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNivm(RPackage):
	"""Noninferiority Tests with Variable Margins

	Noninferiority tests for difference in failure rates at a prespecified control rate or prespecified time. For details, see Fay and Follmann, 2016 <DOI:10.1177/1740774516654861>.
	"""
	
	cran = "nivm" 

	version("0.5", md5="4abb16696ea6ec7ffbb36c634f971d38")

	depends_on("r-bpcp", type=("build", "run"))
	depends_on("r-ssanv", type=("build", "run"))
