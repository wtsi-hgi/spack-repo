# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRltp(RPackage):
	"""R Interface to the 'LTP'-Cloud Service

	R interface to the 'LTP'-Cloud service for Natural Language Processing
    in Chinese (http://www.ltp-cloud.com/).
	"""
	
	homepage = "https://github.com/hetong007/rLTP"
	cran = "rLTP" 

	version("0.1.4", md5="38b35665590d69d9ae94ee30183ef353")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
