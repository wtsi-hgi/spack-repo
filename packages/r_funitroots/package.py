# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunitroots(RPackage):
	"""Rmetrics - Modelling Trends and Unit Roots

	Provides four addons for analyzing trends and
    unit roots in financial time series: (i) functions for the density
    and probability of the augmented Dickey-Fuller Test, (ii) functions 
    for the density and probability of MacKinnon's unit root test 
    statistics, (iii) reimplementations for the ADF and MacKinnon
    Test, and (iv) an 'urca' Unit Root Test Interface for Pfaff's
    unit root test suite.
	"""
	
	homepage = "https://r-forge.r-project.org/scm/viewvc.php/pkg/fUnitRoots/?root=rmetrics"
	cran = "fUnitRoots" 

	version("4021.80", md5="16d17521086f502bacd13bfda5150190")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
