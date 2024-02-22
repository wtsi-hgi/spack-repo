# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgclassification(RPackage):
	"""Gabriel Graph Based Large-Margin Classifiers

	Contains the implementation of a binary large margin classifier based on Gabriel Graph. References for this method can be found in L.C.B. Torres et al. (2015) <doi:10.1049/el.2015.1644>.
	"""
	
	cran = "GGClassification" 

	version("0.1", md5="be60e6fa36e93021a45599bc0f9183c3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
