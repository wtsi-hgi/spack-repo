# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFairsubset(RPackage):
	"""Choose Representative Subsets

	Allows user to obtain subsets of columns of data or vectors within a list.  These subsets will match the original data in terms of average and variation, but have a consistent length of data per column.  It is intended for use on automated data generation which may not always output the same N per replicate or sample.
	"""
	
	homepage = "https://pubmed.ncbi.nlm.nih.gov/31583263/"
	cran = "fairsubset" 

	version("1.0", md5="1827e94c8d7ee986f430d11723990e1f")

	depends_on("r-matrixstats", type=("build", "run"))
