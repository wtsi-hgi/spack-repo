# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmb(RPackage):
	"""Arbitrary Dependency Mixed Multivariate Bayesian Models

	Supports Bayesian models with full and partial (hence
    arbitrary) dependencies between random variables. Discrete and continuous
    variables are supported, and conditional joint probabilities and probability
    densities are estimated using Kernel Density Estimation (KDE). The full
    general form, which implements an extension to Bayes' theorem, as well as
    the simple form, which is just a Bayesian network, both support regression
    through segmentation and KDE and estimation of probability or relative
    likelihood of discrete or continuous target random variables. This package
    also provides true statistical distance measures based on Bayesian models.
    Furthermore, these measures can be facilitated on neighborhood searches,
    and to estimate the similarity and distance between data points.
    Related work is by Bayes (1763) <doi:10.1098/rstl.1763.0053>
    and by Scutari (2010) <doi:10.18637/jss.v035.i03>.
	"""
	
	homepage = "https://github.com/MrShoenel/R-mmb"
	cran = "mmb" 

	version("0.13.3", md5="5af91503e355b91265d5c8ca928dac90")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
