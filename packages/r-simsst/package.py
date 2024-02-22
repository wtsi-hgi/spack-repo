# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimsst(RPackage):
	"""Simulated Stop Signal Task Data

	Stop signal task  data of go and stop trials is generated per participant. The simulation process is based on the generally non-independent horse race model and fixed stop signal delay or tracking method. Each of go and stop process is assumed having exponentially modified Gaussian(ExG) or Shifted Wald (SW) distributions. The output data can be converted to 'BEESTS' software input data enabling researchers to test and evaluate various brain stopping processes manifested by ExG or SW distributional parameters of interest. Methods are described in: Soltanifar M (2020) <https://hdl.handle.net/1807/101208>, Matzke D, Love J, Wiecki TV, Brown SD, Logan GD and Wagenmakers E-J (2013) <doi:10.3389/fpsyg.2013.00918>, Logan GD, Van Zandt T, Verbruggen F, Wagenmakers EJ. (2014) <doi:10.1037/a0035230>.
	"""
	
	cran = "SimSST" 

	version("0.0.5.2", md5="e72d55008f0419bb3beec5e0b73314f6")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
