# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhsdb(RPackage):
	"""Ryan-Holm Step-Down Bonferroni or Sidak Procedure

	The Ryan-Holm step-down Bonferroni or Sidak procedure is to control the family-wise (experiment-wise) type I error rate in the multiple comparisons.
    This procedure provides the adjusting p-values and adjusting CIs. The methods used in this package are referenced from John Ludbrook (2000) <doi:10.1046/j.1440-1681.2000.03223.x>.  
	"""
	
	cran = "RHSDB" 

	version("0.2.0", md5="c58042023a9c835602f985a8c588ee25")

