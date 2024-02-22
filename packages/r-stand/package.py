# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStand(RPackage):
	"""Statistical Analysis of Non-Detects

	Provides functions for the analysis of
        occupational and environmental data with non-detects. Maximum
        likelihood (ML) methods for censored log-normal data and
        non-parametric methods based on the product limit estimate (PLE)
        for left censored data are used to calculate all of the
        statistics recommended by the American Industrial Hygiene
        Association (AIHA) for the complete data case. Functions for
        the analysis of complete samples using exact methods are also
        provided for the lognormal model. Revised from 2007-11-05
        'survfit~1'.
	"""
	
	homepage = "http://www.csm.ornl.gov/esh/statoed/"
	cran = "STAND" 

	version("2.0", md5="5788682af24258ed4a9fc3d0b94d1b4a")

	depends_on("r-survival", type=("build", "run"))
