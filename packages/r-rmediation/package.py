# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmediation(RPackage):
	"""Mediation Analysis Confidence Intervals

	We provide functions to compute confidence intervals for a well-defined nonlinear function of the model parameters (e.g., product of k coefficients) in single--level and
    multilevel structural equation models. It also computes a chi-square test statistic for a function of indirect effects. 
    'Tofighi', D. and 'MacKinnon', D. P. (2011). 'RMediation' An R package for mediation analysis confidence intervals. Behavior Research Methods, 43, 692--700. <doi:10.3758/s13428-011-0076-x>.
    'Tofighi', D. (2020). Bootstrap Model-Based Constrained Optimization Tests of Indirect Effects. Frontiers in Psychology, 10, 2989. <doi:10.3389/fpsyg.2019.02989>.
	"""
	
	cran = "RMediation" 

	version("1.2.2", md5="8e4320fa57e59c48fe3a495b294617d9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan@0.5.20:", type=("build", "run"))
	depends_on("r-e1071@1.6.7:", type=("build", "run"))
	depends_on("r-openmx@2.13:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-modelr@0.1.4:", type=("build", "run"))
	depends_on("r-doparallel@1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-iterators@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
