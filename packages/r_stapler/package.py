# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStapler(RPackage):
	"""Simultaneous Truth and Performance Level Estimation

	An implementation of Simultaneous Truth and 
    Performance Level Estimation (STAPLE) <doi:10.1109/TMI.2004.828354>.  This
    method is used when there are multiple raters for an object, typically an
    image, and this method fuses these ratings into one rating.  It uses an
    expectation-maximization method to estimate this rating and the individual
    specificity/sensitivity for each rater.
	"""
	
	homepage = "https://github.com/muschellij2/stapler"
	cran = "stapler" 

	version("0.7.1", md5="dd86aeb04d35cbbb666f1bcc9d8bcc37")

	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
