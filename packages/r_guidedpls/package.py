# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuidedpls(RPackage):
	"""Supervised Dimensional Reduction by Guided Partial Least Squares

	Guided partial least squares (guided-PLS) is the combination of partial least squares by singular value decomposition (PLS-SVD) and guided principal component analysis (guided-PCA). For the details of the methods, see the reference section of GitHub README.md <https://github.com/rikenbit/guidedPLS>.
	"""
	
	homepage = "https://github.com/rikenbit/guidedPLS"
	cran = "guidedPLS" 

	version("1.0.0", md5="8921bc8795600e5362f907e5b0098dc8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
