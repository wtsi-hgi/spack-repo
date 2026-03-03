# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrcovna(RPackage):
	"""Scalable Robust Estimators with High Breakdown Point for
Incomplete Data

	Robust Location and Scatter Estimation and Robust
        Multivariate Analysis with High Breakdown Point for Incomplete
        Data (missing values) (Todorov et al. (2010) <doi:10.1007/s11634-010-0075-2>).
	"""
	
	homepage = "https://github.com/valentint/rrcovNA"
	cran = "rrcovNA" 

	version("0.5-1", md5="a331e5531c02609e9d330a2e3fb4e95e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rrcov@1.3.7:", type=("build", "run"))
	depends_on("r-robustbase@0.92.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
