# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcttdnn(RPackage):
	"""Cointegration Based Timedelay Neural Network Model

	This cointegration based Time Delay Neural Network Model hybrid model allows the researcher to make use of the information extracted by the cointegrating vector as an input in the neural network model.
	"""
	
	cran = "ECTTDNN" 

	version("0.1.0", md5="0a7ad802ceccd8639f60d46544f46240")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
