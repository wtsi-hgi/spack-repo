# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonmlp(RPackage):
	"""Multi-Layer Perceptron Neural Network with Optional Monotonicity
Constraints

	Train and make predictions from a multi-layer perceptron neural
        network with optional partial monotonicity constraints.
	"""
	
	cran = "monmlp" 

	version("1.1.5", md5="56347a6e2615ad3a761f64ebbf8ea75a")

	depends_on("r-optimx", type=("build", "run"))
