# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetr(RPackage):
	"""Suite of Deterministic and Robust Algorithms for Linear
Regression

	DetLTS, DetMM (and DetS) Algorithms for Deterministic, Robust
    Linear Regression.
	"""
	
	cran = "DetR" 

	version("0.0.5", md5="54d5ad5e0688e5f0a8ad5350520f59ba")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-rcpp@0.10.5:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.2:", type=("build", "run"))
