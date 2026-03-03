# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlatformdesign(RPackage):
	"""Optimal Two-Period Multiarm Platform Design with New
Experimental Arms Added During the Trial

	Design parameters of the optimal two-period multiarm platform design
    (controlling for either family-wise error rate or pair-wise error rate) can be calculated
    using this package, allowing pre-planned deferred arms to be added during the trial. More
    details about the design method can be found in the paper: Pan, H., Yuan, X. and Ye, J.
    (2022) "An optimal two-period multiarm platform design with new experimental arms added
    during the trial". Manuscript submitted for publication. For additional references: Dunnett,
    C. W. (1955) <doi:10.2307/2281208>.
	"""
	
	cran = "PlatformDesign" 

	version("2.1.4", md5="0783de9f91e1907c7359a2e8f891243e")

	depends_on("r-mvtnorm", type=("build", "run"))
