# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoeclust(RPackage):
	"""Gaussian Parsimonious Clustering Models with Covariates and a
Noise Component

	Clustering via parsimonious Gaussian Mixtures of Experts using the MoEClust models introduced by Murphy and Murphy (2020) <doi:10.1007/s11634-019-00373-8>. This package fits finite Gaussian mixture models with a formula interface for supplying gating and/or expert network covariates using a range of parsimonious covariance parameterisations from the GPCM family via the EM/CEM algorithm. Visualisation of the results of such models using generalised pairs plots and the inclusion of an additional noise component is also facilitated. A greedy forward stepwise search algorithm is provided for identifying the optimal model in terms of the number of components, the GPCM covariance parameterisation, and the subsets of gating/expert network covariates.
	"""
	
	homepage = "https://cran.r-project.org/package=MoEClust"
	cran = "MoEClust" 

	version("1.5.2", md5="bbd3ec5d6de875fa59deb9fb98c434e7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lattice@0.12:", type=("build", "run"))
	depends_on("r-matrixstats@1:", type=("build", "run"))
	depends_on("r-mclust@5.4:", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-nnet@7.3.0:", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
