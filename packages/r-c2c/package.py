# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC2c(RPackage):
	"""Compare Two Classifications or Clustering Solutions of Varying
Structure

	Compare two classifications or clustering solutions that may or may
    not have the same number of classes, and that might have hard or soft
    (fuzzy, probabilistic) membership. Calculate various metrics to assess how
    the clusters compare to each other. The calculations are simple, but provide
    a handy tool for users unfamiliar with matrix multiplication. This package
    is not geared towards traditional accuracy assessment for classification/
    mapping applications - the motivating use case is for comparing a
    probabilistic clustering solution to a set of reference or existing class
    labels that could have any number of classes (that is, without having to
    degrade the probabilistic clustering to hard classes).
	"""
	
	homepage = "https://github.com/mitchest/c2c/"
	cran = "c2c" 

	version("0.1.0", md5="1ea336502aa17f44c1396e8ef3778094")

	depends_on("r@3.1:", type=("build", "run"))
