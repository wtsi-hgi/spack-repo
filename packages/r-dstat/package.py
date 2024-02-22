# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDstat(RPackage):
	"""Conditional Sensitivity Analysis for Matched Observational
Studies

	A d-statistic tests the null hypothesis of no treatment effect in a matched, nonrandomized study of the effects caused by treatments.  A d-statistic focuses on subsets of matched pairs that demonstrate insensitivity to unmeasured bias in such an observational study, correcting for double-use of the data by conditional inference. This conditional inference can, in favorable circumstances, substantially increase the power of a sensitivity analysis (Rosenbaum (2010) <doi:10.1007/978-1-4419-1213-8_14>).  There are two examples, one concerning unemployment from Lalive et al. (2006) <doi:10.1111/j.1467-937X.2006.00406.x>, the other concerning smoking and periodontal disease from Rosenbaum (2017) <doi:10.1214/17-STS621>.  
	"""
	
	cran = "dstat" 

	version("1.0.4", md5="50f1b2479ee50eb903c3b5f210861993")

