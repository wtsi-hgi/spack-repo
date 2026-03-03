# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExceedprob(RPackage):
	"""Confidence Intervals for Exceedance Probability

	Computes confidence intervals for the exceedance probability of normally distributed estimators. Currently only supports general linear models. Please see Segal (2019) <arXiv:1803.03356> for more information.
	"""
	
	homepage = "https://github.com/bdsegal/exceedProb"
	cran = "exceedProb" 

	version("0.0.1", md5="bc817c4abd5078230d2b9bb9a26869b1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
