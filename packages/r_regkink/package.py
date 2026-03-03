# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegkink(RPackage):
	"""Regression Kink with a Time-Varying Threshold

	An algorithm is proposed to estimate regression kink model proposed by the paper, Lixiong Yang and Jen-Je Su (2018) <doi:10.1016/j.jimonfin.2018.06.002>.
	"""
	
	cran = "RegKink" 

	version("0.1.0", md5="8b3a811c32726e49d64f656a167287e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
