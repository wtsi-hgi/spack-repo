# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvx(RPackage):
	"""Robust Econometric Inference

	Drawing statistical inference on the coefficients
    of a short- or long-horizon predictive regression with persistent
    regressors by using the IVX method of Magdalinos and Phillips (2009)
    <doi:10.1017/S0266466608090154> and Kostakis, Magdalinos and
    Stamatogiannis (2015) <doi:10.1093/rfs/hhu139>.
	"""
	
	homepage = "https://github.com/kvasilopoulos/ivx"
	cran = "ivx" 

	version("1.1.0", md5="15dc38129cb6201ab5ab411503a19573")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp@1.0.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.300.2:", type=("build", "run"))
