# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsna(RPackage):
	"""Tools for Temporal Social Network Analysis

	Temporal SNA tools for continuous- and discrete-time longitudinal networks having vertex, edge, and attribute dynamics stored in the 'networkDynamic' format. This work was supported by grant R01HD68395 from the National Institute of Health.
	"""
	
	homepage = "http://statnet.org/"
	cran = "tsna" 

	version("0.3.5", md5="e7154722347e80fee13f7de88cee9470")

	depends_on("r-network@1.13:", type=("build", "run"))
	depends_on("r-networkdynamic@0.9:", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
