# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsw(RPackage):
	"""Fitting a Log-Binomial Model using the Bekhit-Schöpe-Wagenpfeil
(BSW) Algorithm

	Implements a modified Newton-type algorithm (BSW algorithm) for solving the maximum likelihood estimation problem in fitting a log-binomial model under linear inequality constraints.
	"""
	
	homepage = "https://github.com/adam-bec/BSW"
	cran = "BSW" 

	version("0.1.1", md5="405a31c88f86122f9082ffb7d4a729ad")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
