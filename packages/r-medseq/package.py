# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedseq(RPackage):
	"""Mixtures of Exponential-Distance Models with Covariates

	Implements a model-based clustering method for categorical life-course sequences relying on mixtures of exponential-distance models introduced by Murphy et al. (2021) <doi:10.1111/rssa.12712>. A range of flexible precision parameter settings corresponding to weighted generalisations of the Hamming distance metric are considered, along with the potential inclusion of a noise component. Gating covariates can be supplied in order to relate sequences to baseline characteristics and sampling weights are also accommodated. The models are fitted using the EM algorithm and tools for visualising the results are also provided.
	"""
	
	homepage = "https://cran.r-project.org/package=MEDseq"
	cran = "MEDseq" 

	version("1.4.1", md5="2d1a15003082fcb8dcad541314d0a11e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-matrixstats@1:", type=("build", "run"))
	depends_on("r-nnet@7.3.0:", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-traminer@1.6:", type=("build", "run"))
	depends_on("r-weightedcluster", type=("build", "run"))
