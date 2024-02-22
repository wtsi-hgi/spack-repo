# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHhp(RPackage):
	"""Hierarchical Heterogeneity Analysis via Penalization

	In medical research, supervised heterogeneity analysis has important implications. Assume that there are two types of features. Using both types of features, our goal is to conduct the first supervised heterogeneity analysis that satisfies a hierarchical structure. That is, the first type of features defines a rough structure, and the second type defines a nested and more refined structure. A penalization approach is developed, which has been motivated by but differs significantly from penalized fusion and sparse group penalization. 
             Reference: 
             Ren, M., Zhang, Q., Zhang, S., Zhong, T., Huang, J. & Ma, S. (2022). "Hierarchical cancer heterogeneity analysis based on histopathological imaging features". Biometrics, <doi:10.1111/biom.13426>.
	"""
	
	cran = "HhP" 

	version("1.0.0", md5="3881edce3c3e6cd30e991ec334ba66c8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fmrs", type=("build", "run"))
