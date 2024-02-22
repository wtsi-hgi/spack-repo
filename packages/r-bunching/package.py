# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBunching(RPackage):
	"""Estimate Bunching

	Implementation of the bunching estimator for kinks and notches. 
        Allows for flexible estimation of counterfactual (e.g. controlling for round number bunching, accounting for other bunching masses within bunching window, fixing bunching point to be minimum, maximum or median value in its bin, etc.). 
        It produces publication-ready plots in the style followed since Chetty et al. (2011) <doi:10.1093/qje/qjr013>, with lots of functionality to set plot options.
	"""
	
	homepage = "https://github.com/mavpanos/bunching"
	cran = "bunching" 

	version("0.8.6", md5="023d9d41c3818f0be7264ca878219f71")

	depends_on("r-bb@2014.10.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
