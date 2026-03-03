# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcessag(RPackage):
	"""Stock Assessment Graphs Database Web Services

	R interface to access the web services of the ICES Stock Assessment
             Graphs database <https://sg.ices.dk>.
	"""
	
	homepage = "https://sg.ices.dk"
	cran = "icesSAG" 

	version("1.4.1", md5="0f4231227b58ebfc44d78a261b79bdba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-icesvocab", type=("build", "run"))
