# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCapushe(RPackage):
	"""CAlibrating Penalities Using Slope HEuristics

	Calibration of penalized criteria for model selection. The calibration methods available are based on the slope heuristics.
	"""
	
	homepage = "http://www.math.u-psud.fr/~brault/capushe.html"
	cran = "capushe" 

	version("1.1.2", md5="c80cfe276d1f4f27bf3ff80ac1872232")

	depends_on("r-mass", type=("build", "run"))
