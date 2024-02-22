# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdahuber(RPackage):
	"""Adaptive Huber Estimation and Regression

	Huber-type estimation for mean, covariance and (regularized) regression. For all the methods, the robustification parameter tau is chosen by a tuning-free principle.
	"""
	
	homepage = "https://github.com/XiaoouPan/adaHuber"
	cran = "adaHuber" 

	version("1.1", md5="a3f471539364b4b28634b189f72d8b4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.850.1:", type=("build", "run"))
