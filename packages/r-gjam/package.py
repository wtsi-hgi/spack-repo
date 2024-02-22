# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGjam(RPackage):
	"""Generalized Joint Attribute Modeling

	Analyzes joint attribute data (e.g., species abundance) that are combinations of continuous and discrete data with Gibbs sampling.  Full model and computation details are described in Clark et al. (2018) <doi:10.1002/ecm.1241>.
	"""
	
	cran = "gjam" 

	version("2.6.2", md5="d7378ef450751f6af026833d548efbe7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
