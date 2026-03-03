# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcdanalyze(RPackage):
	"""Design and Analyze Studies using the Sequential Parallel
Comparison Design

	Programs to find the sample size or power of studies using the 
    Sequential Parallel Comparison Design (SPCD) and programs to analyze 
    such studies. This is a clinical trial design where 
    patients initially on placebo who did not respond are re-randomized between 
    placebo and active drug in a second phase and the results of the two phases are 
    pooled. The method of analyzing binary data with this design is described in 
    Fava,Evins, Dorer and Schoenfeld(2003) <doi:10.1159/000069738>, and the 
    method of analyzing continuous data is described in Chen, Yang, 
    Hung and Wang (2011) <doi:10.1016/j.cct.2011.04.006>.
	"""
	
	cran = "SPCDAnalyze" 

	version("0.1.0", md5="fbba8c02e2d0c615044c8673496d4671")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
