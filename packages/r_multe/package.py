# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulte(RPackage):
	"""Multiple Treatment Effects Regression

	Implements contamination bias diagnostics and alternative
    estimators for regressions with multiple treatments. The implementation is
    based on Goldsmith-Pinkham, Hull, and Kolesár (2022) <arXiv:2106.05024>.
	"""
	
	homepage = "https://github.com/kolesarm/multe"
	cran = "multe" 

	version("1.0.0", md5="85156dbc4c9b1a2e1fb3ba50f1b701ca")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
