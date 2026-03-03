# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiplot(RPackage):
	"""Functions to Plot Confidence Interval

	Plot confidence interval from the objects of statistical tests such as
  t.test(), var.test(), cor.test(), prop.test() and fisher.test() ('htest' class),
  Tukey test [TukeyHSD()], Dunnett test [glht() in 'multcomp' package],
  logistic regression [glm()], and Tukey or Games-Howell test [posthocTGH() in
  'userfriendlyscience' package].
  Users are able to set the styles of lines and points.
  This package contains the function to calculate odds ratios and their confidence
  intervals from the result of logistic regression.
	"""
	
	homepage = "https://github.com/toshi-ara/CIplot"
	cran = "CIplot" 

	version("1.0", md5="b5e5711214be52d26fe3a57173d4ca0e")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
