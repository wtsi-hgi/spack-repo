# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcs(RPackage):
	"""Recreates Some 'SAS®' Procedures in 'R'

	Contains functions to simulate the most commonly used 
    'SAS®' procedures.  Specifically, the package aims to 
    simulate the functionality of 'proc freq', 'proc means', 'proc ttest',
    'proc reg', 'proc transpose', 'proc sort', and 'proc print'. 
    The simulation will include recreating 
    all statistics with the highest fidelity possible. 
	"""
	
	homepage = "https://procs.r-sassy.org"
	cran = "procs" 

	version("1.0.6", md5="71529ccda33810993500b365770973ed")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-common", type=("build", "run"))
	depends_on("r-fmtr", type=("build", "run"))
	depends_on("r-reporter", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-saslm@0.9.9:", type=("build", "run"))
