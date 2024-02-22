# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongpower(RPackage):
	"""Sample Size Calculations for Longitudinal Data

	Compute power and sample size for linear models of longitudinal
    data. Supported models include mixed-effects models and models fit by
    generalized least squares and generalized estimating equations. The package
    is described in Iddi and Donohue (2022) <DOI:10.32614/RJ-2022-022>. Relevant
    formulas are derived by Liu and Liang (1997) <DOI:10.2307/2533554>, 
    Diggle et al (2002) <ISBN:9780199676750>, and Lu, Luo, and Chen (2008)
    <DOI:10.2202/1557-4679.1098>.
	"""
	
	homepage = "https://github.com/mcdonohue/longpower"
	cran = "longpower" 

	version("1.0.25", md5="c829e315c8b5e828e4aa92d89ad68795")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
