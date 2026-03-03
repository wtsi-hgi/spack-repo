# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTest2norm(RPackage):
	"""Normative Standards for Cognitive Tests

	Package test2norm contains functions to generate formulas for 
    normative standards applied to cognitive tests. It takes raw test scores 
    (e.g., number of correct responses) and converts them to scaled scores and 
    demographically adjusted scores, using methods described in Heaton et al. 
    (2003) <doi:10.1016/B978-012703570-3/50010-9> & Heaton et al. (2009, 
    ISBN:9780199702800). The scaled scores are calculated as quantiles of the 
    raw test scores, scaled to have the mean of 10 and standard deviation of 3, 
    such that higher values always correspond to better performance on the test. 
    The demographically adjusted scores are calculated from the residuals of a 
    model that regresses scaled scores on demographic predictors (e.g., age). 
    The norming procedure makes use of the mfp() function from the 'mfp' package 
    to explore nonlinear associations between cognition and demographic 
    variables.
	"""
	
	cran = "test2norm" 

	version("0.2.1", md5="9ad1bd995d6511c8f41b18d1ad06bb73")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mfp", type=("build", "run"))
