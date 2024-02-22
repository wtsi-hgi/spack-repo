# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongroc(RPackage):
	"""Time-Dependent Prognostic Accuracy with Multiply Evaluated Bio
Markers or Scores

	Time-dependent Receiver Operating Characteristic curves, Area Under the Curve, and Net Reclassification Indexes for repeated measures. It is based on methods in Barbati and Farcomeni (2017) <doi:10.1007/s10260-017-0410-2>. 
	"""
	
	cran = "longROC" 

	version("1.0", md5="9736d2eab315c0c22ab3a533d29d8790")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
