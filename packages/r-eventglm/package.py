# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventglm(RPackage):
	"""Regression Models for Event History Outcomes

	A user friendly, easy to understand way of doing event
    history regression for marginal estimands of interest,
    including the cumulative incidence and the restricted mean
    survival, using the pseudo observation framework for 
    estimation. For a review of the methodology, see Andersen and
    Pohar Perme (2010) <doi:10.1177/0962280209105020> or Sachs 
    and Gabriel (2022) <doi:10.18637/jss.v102.i09>. The
    interface uses the well known formulation of a generalized
    linear model and allows for features including plotting of 
    residuals, the use of sampling weights, and corrected
    variance estimation. 
	"""
	
	homepage = "https://sachsmc.github.io/eventglm/"
	cran = "eventglm" 

	version("1.2.2", md5="084cc4f1b15ff3b44ef9f1eb7c3434e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
