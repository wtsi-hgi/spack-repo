# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhmsar(RPackage):
	"""Non-Homogeneous Markov Switching Autoregressive Models

	Calibration, simulation, validation of (non-)homogeneous Markov switching autoregressive models with Gaussian or von Mises innovations.  Penalization methods are implemented for Markov Switching Vector Autoregressive Models of order 1 only. Most functions of the package handle missing values.
	"""
	
	cran = "NHMSAR" 

	version("1.19", md5="9b7f304326eae37a466f6c88c11be0fc")

	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
