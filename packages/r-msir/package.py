# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsir(RPackage):
	"""Model-Based Sliced Inverse Regression

	An R package for dimension reduction based on finite Gaussian mixture modeling of inverse regression.
	"""
	
	homepage = "https://mclust-org.github.io/msir/"
	cran = "msir" 

	version("1.3.3", md5="1bc8ec08f0420a27c03ba01512b4bb7f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mclust@5.4:", type=("build", "run"))
