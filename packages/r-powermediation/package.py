# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowermediation(RPackage):
	"""Power/Sample Size Calculation for Mediation Analysis

	Functions to 
        calculate power and sample size for testing
        (1) mediation effects; 
        (2) the slope in a simple linear regression; 
        (3) odds ratio in a simple logistic regression;
        (4) mean change for longitudinal study with 2 time points;
        (5) interaction effect in 2-way ANOVA; and
        (6) the slope in a simple Poisson regression.
	"""
	
	cran = "powerMediation" 

	version("0.3.4", md5="d3b0506f06fe8259dba6bc511131fa05")

	depends_on("r@3.5:", type=("build", "run"))
