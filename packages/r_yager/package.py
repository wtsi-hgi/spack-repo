# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYager(RPackage):
	"""Yet Another General Regression Neural Network

	Another implementation of general regression neural network in R
    based on Specht (1991) <DOI:10.1109/72.97934>. It is applicable to the 
    functional approximation or the classification. 
	"""
	
	homepage = "https://github.com/statcompute/yager"
	cran = "yager" 

	version("0.1.1", md5="c084b425c1501b193baac52ccef9a34e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
