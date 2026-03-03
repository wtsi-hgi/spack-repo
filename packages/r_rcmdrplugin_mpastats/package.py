# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginMpastats(RPackage):
	"""R Commander Plug-in for MPA Statistics

	Extends R Commander with a unified menu of new and pre-existing 
        statistical functions related to public management and policy analysis 
        statistics. Functions and menus have been renamed according to the 
        usage in PMGT 630 in the Master of Public Administration program at
        Brigham Young University.
	"""
	
	cran = "RcmdrPlugin.MPAStats" 

	version("1.2.2", md5="371496952c3cadc52959ffdc22cdf5a2")

	depends_on("r-rcmdr@1.4.0:", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
