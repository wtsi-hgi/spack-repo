# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparklyrFlint(RPackage):
	"""Sparklyr Extension for 'Flint'

	This sparklyr extension makes 'Flint' time series
    library functionalities (<https://github.com/twosigma/flint>) easily
    accessible through R.
	"""
	
	homepage = "<https://github.com/r-spark/sparklyr.flint>"
	cran = "sparklyr.flint" 

	version("0.2.2", md5="6fc51309bd644d83eede934dcc050c8d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sparklyr@1.3:", type=("build", "run"))
	depends_on("spark@2:", type=("build", "link", "run"))
