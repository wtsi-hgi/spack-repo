# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssistant(RPackage):
	"""Adaptive Subgroup Selection in Group Sequential Trials

	Clinical trial design for subgroup selection in three-stage group
             sequential trial as described in Lai, Lavori and Liao (2014,
	     <doi:10.1016/j.cct.2014.09.001>). Includes facilities for design,
	     exploration and analysis of such trials. An implementation of
	     the initial DEFUSE-3 trial is also provided as a vignette.
	"""
	
	homepage = "https://github.com/bnaras/ASSISTant"
	cran = "ASSISTant" 

	version("1.4.3", md5="45f788a9c4336c4b7f80775a5d41da26")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
