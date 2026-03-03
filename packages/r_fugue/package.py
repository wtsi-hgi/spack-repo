# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFugue(RPackage):
	"""Sensitivity Analysis Optimized for Matched Sets of Varied Sizes

	As in music, a fugue statistic repeats a theme in small variations.  Here, the psi-function that defines an m-statistic is slightly altered to maintain the same design sensitivity in matched sets of different sizes.  The main functions in the package are sen() and senCI().  For sensitivity analyses for m-statistics, see Rosenbaum (2007) Biometrics 63 456-464 <doi:10.1111/j.1541-0420.2006.00717.x>.
	"""
	
	cran = "fugue" 

	version("0.1.7", md5="95c4dc949cf918d38b845827214f5036")

