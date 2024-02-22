# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBibs(RPackage):
	"""Bayesian Inference for the Birnbaum-Saunders Distribution

	Developed for the following tasks. 1- Simulating and computing the maximum likelihood 
              estimator for the Birnbaum-Saunders (BS) distribution, 2- Computing the Bayesian estimator for
              the parameters of the BS distribution based on reference prior proposed by Xu and Tang (2010)
              <doi:10.1016/j.csda.2009.08.004> and conjugate prior. 3- Computing the Bayesian estimator for
              the BS distribution based on conjugate prior. 4- Computing the Bayesian estimator for the BS
              distribution based on Jeffrey prior given by Achcar (1993) <doi:10.1016/0167-9473(93)90170-X>
              5- Computing the Bayesian estimator for the BS distribution under progressive type-II censoring
              scheme.
	"""
	
	cran = "bibs" 

	version("1.1.1", md5="8c495dd7b03d75384e15e7f10a085d85")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
