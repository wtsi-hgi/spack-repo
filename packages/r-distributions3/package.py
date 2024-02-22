# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistributions3(RPackage):
	"""Probability Distributions as S3 Objects

	Tools to create and manipulate probability distributions
    using S3.  Generics pdf(), cdf(), quantile(), and random() provide
    replacements for base R's d/p/q/r style functions.  Functions and
    arguments have been named carefully to minimize confusion for students
    in intro stats courses. The documentation for each distribution
    contains detailed mathematical notes.
	"""
	
	homepage = "https://github.com/alexpghayes/distributions3"
	cran = "distributions3" 

	version("0.2.1", md5="de2560c8cfa8a5ffa9ee9e0bcd7f745a", url="https://cran.r-project.org/src/contrib/distributions3_0.2.1.tar.gz")

	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
