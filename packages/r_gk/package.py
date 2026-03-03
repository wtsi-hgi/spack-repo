# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGk(RPackage):
	"""g-and-k and g-and-h Distribution Functions

	Functions for the g-and-k and generalised g-and-h distributions.
	"""
	
	homepage = "https://github.com/dennisprangle/gk"
	cran = "gk" 

	version("0.6.0", md5="99826cb6163afce02c8c205e9da8ff70")

	depends_on("r-ecdat", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
