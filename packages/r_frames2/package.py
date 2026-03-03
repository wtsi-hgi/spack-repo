# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrames2(RPackage):
	"""Estimation in Dual Frame Surveys

	Point and interval estimation in dual frame surveys. In contrast
    to classic sampling theory, where only one sampling frame is considered,
    dual frame methodology assumes that there are two frames available for
    sampling and that, overall, they cover the entire target population. Then,
    two probability samples (one from each frame) are drawn and information
    collected is suitably combined to get estimators of the parameter of
    interest.
	"""
	
	cran = "Frames2" 

	version("0.2.1", md5="bd5075393975fd7d9cf3eef9e4cbeee7", url="https://cran.r-project.org/src/contrib/Frames2_0.2.1.tar.gz")

	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
