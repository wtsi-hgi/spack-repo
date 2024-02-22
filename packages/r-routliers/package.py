# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoutliers(RPackage):
	"""Robust Outliers Detection

	Detecting outliers using robust methods, 
 	i.e. the Median Absolute Deviation (MAD) for univariate outliers; Leys, Ley, Klein, Bernard, & Licata (2013) <doi:10.1016/j.jesp.2013.03.013>
        and the Mahalanobis-Minimum Covariance Determinant (MMCD) for multivariate outliers; Leys, C., Klein, O., Dominicy, Y. & Ley, C. (2018) <doi:10.1016/j.jesp.2017.09.011>.
        There is also the more known but less robust Mahalanobis distance method, only for comparison purposes.
	"""
	
	cran = "Routliers" 

	version("0.0.0.3", md5="40f8ee67774b8d41b50143b6c2dd6b20")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
