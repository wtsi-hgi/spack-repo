# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGerbil(RPackage):
	"""Generalized Efficient Regression-Based Imputation with Latent
Processes

	Implements a new multiple imputation method that draws
    imputations from a latent joint multivariate normal model which
    underpins generally structured data. This model is constructed using a
    sequence of flexible conditional linear models that enables the
    resulting procedure to be efficiently implemented on high dimensional
    datasets in practice. See Robbins (2021) <arXiv:2008.02243>.
	"""
	
	cran = "gerbil" 

	version("0.1.9", md5="4a29f86a3ae716af713ef45731dea8b8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
