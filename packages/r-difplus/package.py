# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifplus(RPackage):
	"""Multilevel Mantel-Haenszel Statistics for Differential Item
Functioning Detection

	Clustered or multilevel data structures are common in the assessment of differential item functioning (DIF), particularly in the context of large-scale assessment programs. This package allows users to implement extensions of the Mantel-Haenszel DIF detection procedures in the presence of multilevel data based on the work of Begg (1999) <doi:10.1111/j.0006-341X.1999.00302.x>, Begg & Paykin (2001) <doi:10.1080/00949650108812115>, 
	and French & Finch (2013) <doi:10.1177/0013164412472341>.
	"""
	
	cran = "DIFplus" 

	version("1.1", md5="9d3e2b9345cbe7be2d809d08dba06e2b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-testdataimputation", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
