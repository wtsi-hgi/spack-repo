# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeconvolver(RPackage):
	"""Empirical Bayes Estimation Strategies

	Empirical Bayes methods for learning prior distributions from data.
    An unknown prior distribution (g) has yielded (unobservable) parameters, each of
    which produces a data point from a parametric exponential family (f). The goal
    is to estimate the unknown prior ("g-modeling") by deconvolution and Empirical
    Bayes methods. Details and examples are in the paper by Narasimhan and Efron
    (2020, <doi:10.18637/jss.v094.i11>).
	"""
	
	homepage = "https://bnaras.github.io/deconvolveR/"
	cran = "deconvolveR" 

	version("1.2-1", md5="ef4103db12828a16e918bcab9b096362")

	depends_on("r@3:", type=("build", "run"))
