# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsp(RPackage):
	"""Parameter Space Partitioning MCMC for Global Model Evaluation

	Implements an n-dimensional parameter space partitioning algorithm for evaluating the global behaviour of formal computational models as described by Pitt, Kim, Navarro and Myung (2006) <doi:10.1037/0033-295X.113.1.57>.
	"""
	
	homepage = "https://github.com/lenarddome/psp"
	cran = "psp" 

	version("1.0.0", md5="7eb98f50aa486d5fb1b8f49740b3f55d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
