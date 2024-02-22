# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsmams(RPackage):
	"""Group Sequential Designs of Multi-Arm Multi-Stage Trials

	It provides functions to generate operating characteristics and to calculate Sequential Conditional Probability Ratio Tests(SCPRT) efficacy and futility boundary values along with sample/event size of Multi-Arm Multi-Stage(MAMS) trials for different outcomes. The package is based on Jianrong Wu, Yimei Li, Liang Zhu (2023) <doi:10.1002/sim.9682>, Jianrong Wu, Yimei Li (2023) "Group Sequential Multi-Arm Multi-Stage Survival Trial Design with Treatment Selection"(Manuscript accepted for publication) and Jianrong Wu, Yimei Li, Shengping Yang (2023) "Group Sequential Multi-Arm Multi-Stage Trial Design with Ordinal Endpoints"(In preparation).   
	"""
	
	cran = "gsMAMS" 

	version("0.7.1", md5="5a4f38dc73bb2537df212aaee9dc65a3")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
