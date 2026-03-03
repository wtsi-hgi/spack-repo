# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrrcbcv(RPackage):
	"""Bias-Corrected Variance for Competing Risks Regression with
Clustered Data

	
  A user friendly function 'crrcbcv' to compute bias-corrected variances for competing risks regression models using proportional subdistribution hazards with small-sample clustered data. Four types of bias correction are included: the MD-type bias correction by Mancl and DeRouen (2001) <doi:10.1111/j.0006-341X.2001.00126.x>, the KC-type bias correction by Kauermann and Carroll (2001) <doi:10.1198/016214501753382309>, the FG-type bias correction by Fay and Graubard (2001) <doi:10.1111/j.0006-341X.2001.01198.x>, and the MBN-type bias correction by Morel, Bokossa, and Neerchal (2003) <doi:10.1002/bimj.200390021>.
	"""
	
	cran = "crrcbcv" 

	version("1.0", md5="6dc93738e13a4c6dbeac51dafdb98eea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crrsc", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
