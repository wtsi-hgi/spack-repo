# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcdat(RPackage):
	"""Data Sets for Econometrics

	Data sets for econometrics, including political science.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "Ecdat" 

	version("0.4-2", md5="ba4624dfa9e48a22671c3e7fb772ba5e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ecfun", type=("build", "run"))
