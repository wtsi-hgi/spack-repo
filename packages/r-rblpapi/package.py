# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRblpapi(RPackage):
	"""R Interface to 'Bloomberg'

	An R Interface to 'Bloomberg' is provided via the 'Blp API'.
	"""
	
	homepage = "https://dirk.eddelbuettel.com/code/rblpapi.html"
	cran = "Rblpapi" 

	version("0.3.14", md5="b277cfe10dc79e2e4d729f520d74e73e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
