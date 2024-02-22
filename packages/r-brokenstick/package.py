# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrokenstick(RPackage):
	"""Broken Stick Model for Irregular Longitudinal Data

	Data on multiple individuals through time are often sampled at 
    times that differ between persons. Irregular observation times can severely 
    complicate the statistical analysis of the data. The broken stick model 
    approximates each subject’s trajectory by one or more connected line segments. 
    The times at which segments connect (breakpoints) are identical for all 
    subjects and under control of the user. A well-fitting broken stick model 
    effectively transforms individual measurements made at irregular times into 
    regular trajectories with common observation times. Specification of the 
    model requires three variables: time, measurement and subject. The 
    model is a special case of the linear mixed model, with time as a linear 
    B-spline and subject as the grouping factor. The main assumptions are: 
    subjects are exchangeable, trajectories between consecutive breakpoints are 
    straight, random effects follow a multivariate normal distribution, and 
    unobserved data are missing at random. The package contains functions for 
    fitting the broken stick model to data, for predicting curves in new data 
    and for plotting broken stick estimates. The package supports two 
    optimization methods, and includes options to structure the 
    variance-covariance matrix of the random effects. The analyst may use the 
    software to smooth growth curves by a series of connected straight lines, to 
    align irregularly observed curves to a common time grid, to create synthetic 
    curves at a user-specified set of breakpoints, to estimate the time-to-time 
    correlation matrix and to predict future observations. See 
    <doi:10.18637/jss.v106.i07> for additional documentation on background, 
    methodology and applications.
	"""
	
	homepage = "doi:10.18637/jss.v106.i07"
	cran = "brokenstick" 

	version("2.5.0", md5="a189afd79b48a6d493e37045a45b9059")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrixsampling", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
