# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsae(RPackage):
	"""Robust Small Area Estimation

	Empirical best linear unbiased prediction (EBLUP) and
    robust prediction of the area-level means under the basic unit-level
    model. The model can be fitted by maximum likelihood or a (robust)
    M-estimator. Mean square prediction error is computed by a parametric
    bootstrap.
	"""
	
	homepage = "https://github.com/tobiasschoch/rsae"
	cran = "rsae" 

	version("0.3", md5="a5bf4583c13786702342088d51175484")

	depends_on("r@3.5:", type=("build", "run"))
