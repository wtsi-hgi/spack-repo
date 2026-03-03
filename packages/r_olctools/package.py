# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlctools(RPackage):
	"""Open Location Code Handling in R

	'Open Location Codes' <http://openlocationcode.com/>
    are a Google-created standard for identifying geographic locations. 'olctools' provides
    utilities for validating, encoding and decoding entries that follow this
    standard.
	"""
	
	homepage = "https://github.com/Ironholds/olctools"
	cran = "olctools" 

	version("0.3.0", md5="7a35fc590507159e6813469f18e28660")

	depends_on("r-rcpp", type=("build", "run"))
