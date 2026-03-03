# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNomogramformula(RPackage):
	"""Calculate Total Points and Probabilities for Nomogram

	
  A nomogram, which can be carried out in 'rms' package, provides a 
    graphical explanation of a prediction process. However, it is not very easy
    to draw straight lines, read points and probabilities accurately. Even, it 
    is hard for users to calculate total points and probabilities for all 
    subjects.
  This package provides formula_rd() and formula_lp() functions to fit the 
    formula of total points with raw data and linear predictors respectively by
    polynomial regression. Function points_cal() will help you calculate the 
    total points. prob_cal() can be used to calculate the probabilities after
    lrm(), cph() or psm() regression. 
  For more complex condition, interaction or restricted cubic spine, TotalPoints.rms() 
    can be used.
	"""
	
	homepage = "https://github.com/yikeshu0611/nomogramFormula"
	cran = "nomogramFormula" 

	version("1.2.0.0", md5="552ddb326bbff202be3fe31ec2f36ff3")

	depends_on("r-rms", type=("build", "run"))
	depends_on("r-do", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
