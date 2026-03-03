# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstem(RPackage):
	"""Multiple Testing of Local Extrema for Detection of Change Points

	A new approach to detect change points based on smoothing and multiple testing, which is for long data sequence modeled as piecewise constant functions plus stationary Gaussian noise, see Dan Cheng and Armin Schwartzman (2015) <arXiv:1504.06384>.
	"""
	
	homepage = "https://arxiv.org/abs/1504.06384"
	cran = "mSTEM" 

	version("1.0-1", md5="0fe5713db35d9f77d58de847fcb14817")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
