# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaussdiff(RPackage):
	"""Difference measures for multivariate Gaussian probability
density functions

	A collection difference measures for multivariate Gaussian
        probability density functions, such as the Euclidea mean, the
        Mahalanobis distance, the Kullback-Leibler divergence, the
        J-Coefficient, the Minkowski L2-distance, the Chi-square
        divergence and the Hellinger Coefficient.
	"""
	
	homepage = "www.geo.fu-berlin.de/met/ag/clidia/Mitarbeiter/HenningRust/"
	cran = "gaussDiff" 

	version("1.1", md5="3124d915ca536d690eabc92aaab50541")

	depends_on("r@1.8:", type=("build", "run"))
