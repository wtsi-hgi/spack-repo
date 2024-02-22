# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdnn(RPackage):
	"""Longitudinal Data Neural Network

	This is a Neural Network regression model implementation using 'Keras', consisting of 10 Long Short-Term Memory layers that are fully connected along with the rest of the inputs.
	"""
	
	cran = "LDNN" 

	version("1.10", md5="7d3766cd29d95b4026b08ac10df22276")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
