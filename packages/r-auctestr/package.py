# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAuctestr(RPackage):
	"""Statistical Testing for AUC Data

	Performs statistical testing to compare predictive 
	models based on multiple observations of the A' statistic (also known as 
	Area Under the Receiver Operating Characteristic Curve, or AUC). 
	Specifically, it implements a testing method based on the equivalence 
	between the A' statistic and the Wilcoxon statistic. 
	For more information, see Hanley and McNeil (1982) <doi:10.1148/radiology.143.1.7063747>. 
	"""
	
	cran = "auctestr" 

	version("1.0.0", md5="e9610b1aadc82af942855847e58886f3")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
