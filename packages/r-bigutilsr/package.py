# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigutilsr(RPackage):
	"""Utility Functions for Large-scale Data

	Utility functions for large-scale data. For now, package 'bigutilsr'
    mainly includes functions for outlier detection and unbiased PCA projection.
	"""
	
	homepage = "https://github.com/privefl/bigutilsr"
	cran = "bigutilsr" 

	version("0.3.4", md5="49ad25ab76efaab30f5dbaed238f2b31")

	depends_on("r-bigassertr@0.1.1:", type=("build", "run"))
	depends_on("r-bigparallelr@0.2.3:", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
