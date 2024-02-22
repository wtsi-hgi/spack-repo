# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothwin(RPackage):
	"""Soft Windowing on Linear Regression

	The main function in the package utilizes a windowing function in the form of an exponential weighting function to linear models. The bandwidth and sharpness of the window are controlled by two parameters. Then, a series of tests are used to identify the right parameters of the window (see Hamed Haselimashhadi et al (2019) <https://www.biorxiv.org/content/10.1101/656678v1>).
	"""
	
	homepage = "http://hamedhaseli.webs.com"
	cran = "SmoothWin" 

	version("3.0.0", md5="9af8019427d9f78b6bf95eacf4a0e8aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
