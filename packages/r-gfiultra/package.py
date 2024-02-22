# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfiultra(RPackage):
	"""Generalized Fiducial Inference for Ultrahigh-Dimensional
Regression

	Variable selection for ultrahigh-dimensional ("large p small n") linear Gaussian models using a fiducial framework allowing to draw inference on the parameters. Reference: Lai, Hannig & Lee (2015) <doi:10.1080/01621459.2014.931237>.
	"""
	
	homepage = "https://github.com/stla/gfiUltra"
	cran = "gfiUltra" 

	version("1.0.0", md5="43ff31ff92f168021fe64d409deaf8e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sis", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
