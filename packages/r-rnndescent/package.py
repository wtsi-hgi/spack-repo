# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnndescent(RPackage):
	"""Nearest Neighbor Descent Method for Approximate Nearest
Neighbors

	The Nearest Neighbor Descent method for finding approximate
    nearest neighbors by Dong and co-workers (2010)
    <doi:10.1145/1963405.1963487>. Based on the 'Python' package
    'PyNNDescent' <https://github.com/lmcinnes/pynndescent>.
	"""
	
	homepage = "https://jlmelville.github.io/rnndescent/"
	cran = "rnndescent" 

	version("0.1.4", md5="b1e1cbf1764e6c7d893dcaad33d03dc0")
	version("0.1.3", md5="03308741556deffa7ee73e37bc366984")

	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-matrix@1.3.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-sitmo", type=("build", "run"))
