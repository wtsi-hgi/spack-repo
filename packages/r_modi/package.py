# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModi(RPackage):
	"""Multivariate Outlier Detection and Imputation for Incomplete
Survey Data

	Algorithms for multivariate outlier detection when missing values
    occur. Algorithms are based on Mahalanobis distance or data depth.
    Imputation is based on the multivariate normal model or uses nearest
    neighbour donors. The algorithms take sample designs, in particular
    weighting, into account. The methods are described in Bill and Hulliger
    (2016) <doi:10.17713/ajs.v45i1.86>.
	"""
	
	homepage = "https://github.com/martinSter/modi"
	cran = "modi" 

	version("0.1.2", md5="431eec8ffb4b55c130da6a94dc1c39ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass@7.3.50:", type=("build", "run"))
	depends_on("r-norm@1.0.9.5:", type=("build", "run"))
