# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpx(RPackage):
	"""Ensemble of Phalanxes

	An ensemble method for the statistical detection of
    a rare class in two-class classification problems. The method uses an
    ensemble of classifiers where the constituent
    models of the ensemble use disjoint subsets (phalanxes) of explanatory
    variables. We provide an implementation of the phalanx-formation algorithm.
    Please see Tomal et al. (2015) <doi:10.1214/14-AOAS778>,
    Tomal et al. (2016) <doi:10.1021/acs.jcim.5b00663>, and
    Tomal et al. (2019) <arXiv:1706.06971> for more details.
	"""
	
	cran = "EPX" 

	version("1.0.4", md5="7464deb9b146a083c898c1e97b0e9895")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rngtools", type=("build", "run"))
