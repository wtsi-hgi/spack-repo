# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecordlinkage(RPackage):
	"""Record Linkage Functions for Linking and Deduplicating Data Sets

	Provides functions for linking and deduplicating data sets.
  Methods based on a stochastic approach are implemented as well as 
  classification algorithms from the machine learning domain. For details, 
  see our paper "The RecordLinkage Package: Detecting Errors in Data" 
  Sariyar M / Borg A (2010) <doi:10.32614/RJ-2010-017>. 
	"""
	
	cran = "RecordLinkage" 

	version("0.4-12.4", md5="0f35a865cd0590202948af64d1e09452")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-ada", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-data-table@1.7.8:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
