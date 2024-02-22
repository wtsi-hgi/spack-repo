# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbclass(RPackage):
	"""Angle-Based Large-Margin Classifiers

	Multi-category angle-based large-margin classifiers.
    See Zhang and Liu (2014) <doi:10.1093/biomet/asu017> for details.
	"""
	
	homepage = "https://wwenjie.org/abclass"
	cran = "abclass" 

	version("0.4.0", md5="dc2d8fbad0e91d3b09d7c2a0a3e65d56")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
