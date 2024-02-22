# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrada(RPackage):
	"""Bayesian Response-Adaptive Design Analysis

	Provides access to a range of functions for analyzing, applying and visualizing Bayesian response-adaptive trial designs for a binary endpoint. Includes the predictive probability approach and the predictive evidence value designs for binary endpoints.
	"""
	
	cran = "brada" 

	version("1.0", md5="9f51b5b1695356161817b97edb7b6062")

	depends_on("r-fbst", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
