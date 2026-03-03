# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRyacas(RPackage):
	"""R Interface to the 'Yacas' Computer Algebra System

	Interface to the 'yacas' computer algebra system (<http://www.yacas.org/>).
	"""
	
	homepage = "https://github.com/r-cas/ryacas"
	cran = "Ryacas" 

	version("1.1.5", md5="8624d974d315af659258d8e36ec6befd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
