# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogbin(RPackage):
	"""Relative Risk Regression Using the Log-Binomial Model

	Methods for fitting log-link GLMs and GAMs to binomial data,
    including EM-type algorithms with more stable convergence properties than standard methods.
	"""
	
	homepage = "https://github.com/mdonoghoe/logbin"
	cran = "logbin" 

	version("2.0.5", md5="b51273717a1c45de3d3bc0c9a567274f")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-turboem@2021.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-itertools2", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
