# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpsm(RPackage):
	"""Nonparametric Statistical Methods

	Accompanies the book "Nonparametric Statistical Methods Using R" by Kloke and McKean (2014, ISBN:9781439873434).  Includes methods, datasets, and random number generation useful for the study of robust and/or nonparametric statistics.  Emphasizes classical nonparametric methods for a variety of designs --- especially one-sample and two-sample problems.  Includes methods for general scores, including estimation and testing for the two-sample location problem as well as Hogg's adaptive method.
	"""
	
	homepage = "https://github.com/kloke/npsm"
	cran = "npsm" 

	version("1.1.1", md5="e72a4f0159f7fda31a2adbedd5bf5388")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rfit", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
