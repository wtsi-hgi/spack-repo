# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSate(RPackage):
	"""Scientific Analysis of Trial Errors (SATE)

	Bundles functions used to analyze the harmfulness of trial errors in criminal trials.
    Functions in the Scientific Analysis of Trial Errors ('SATE') package help users estimate the 
    probability that a jury will find a defendant guilty given jurors' preferences for a guilty 
    verdict and the uncertainty of that estimate. Users can also compare actual and hypothetical 
    trial conditions to conduct harmful error analysis. The relationship between individual jurors' 
    verdict preferences and the probability that a jury returns a guilty verdict has been studied 
    by Davis (1973) <doi:10.1037/h0033951>; MacCoun & Kerr (1988) <doi:10.1037/0022-3514.54.1.21>, 
    and Devine et el. (2001) <doi:10.1037/1076-8971.7.3.622>, among others.
	"""
	
	cran = "sate" 

	version("2.1.0", md5="3f86cf84a58bfb98c7c0a54f20f0473e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
