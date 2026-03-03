# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REqualtestmi(RPackage):
	"""Examine Measurement Invariance via Equivalence Testing and
Projection Method

	Functions for examining measurement invariance via equivalence testing are included in this package. The traditionally used RMSEA (Root Mean Square Error of Approximation) cutoff values are adjusted based on simulation results. In addition, a projection-based method is implemented to test the equality of latent factor means across groups without assuming the equality of intercepts. For more information, see Yuan, K. H., & Chan, W. (2016) <doi:10.1037/met0000080>, Deng, L., & Yuan, K. H. (2016) <doi:10.1007/s11336-015-9491-8>, and Jiang, G., Mai, Y., & Yuan, K. H. (2017) <doi:10.3389/fpsyg.2017.01823>. 
	"""
	
	cran = "equaltestMI" 

	version("0.6.1", md5="a955126b4ec8a1faa91f7b61c29c96a9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
