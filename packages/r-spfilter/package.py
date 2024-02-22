# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpfilter(RPackage):
	"""Semiparametric Spatial Filtering with Eigenvectors in
(Generalized) Linear Models

	Tools to decompose (transformed) spatial connectivity matrices and perform supervised or unsupervised semiparametric spatial filtering in a regression framework. The package supports unsupervised spatial filtering in standard linear as well as some generalized linear regression models.
	"""
	
	homepage = "https://github.com/sjuhl/spfilteR"
	cran = "spfilteR" 

	version("1.1.5", md5="5aa614dbe3e9ac00059db69493851bba")

	depends_on("r@3.5:", type=("build", "run"))
