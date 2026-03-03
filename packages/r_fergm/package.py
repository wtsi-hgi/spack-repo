# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFergm(RPackage):
	"""Estimation and Fit Assessment of Frailty Exponential Random
Graph Models

	Frailty Exponential Random Graph Models estimated through pseudo likelihood with frailty terms estimated using 'Stan' as per Box-Steffensmeier et. al (2017) <doi:10.7910/DVN/K3D1M2>.
    Goodness of fit for Frailty Exponential Random Graph Models is also available, with easy visualizations for comparison to fit Exponential Random Graph Models.  
	"""
	
	homepage = "http://github.com/benjamin-w-campbell/fergm"
	cran = "fergm" 

	version("1.1.4", md5="43310da4bbfff6050ab2aa6af2748a78")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rstan@2.16.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ergm@3.9:", type=("build", "run"))
	depends_on("r-network@1.13:", type=("build", "run"))
	depends_on("r-extrafont@0.17:", type=("build", "run"))
	depends_on("r-matrixstats@0.52.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
