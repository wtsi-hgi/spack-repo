# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplithalf(RPackage):
	"""Calculate Task Split Half Reliability Estimates

	Estimate the internal consistency of your tasks with a permutation based split-half reliability approach.
    Unofficial release name: "I eat stickers all the time, dude!".
	"""
	
	homepage = "https://github.com/sdparsons/splithalf"
	cran = "splithalf" 

	version("0.8.2", md5="dfa36d3a828c9cfdaa1184373d14aa83")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
