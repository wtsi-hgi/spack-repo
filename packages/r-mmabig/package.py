# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmabig(RPackage):
	"""Multiple Mediation Analysis for Big Data Sets

	Used for general multiple mediation analysis with big data sets. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "mmabig" 

	version("3.2-0", md5="b28af678a3cecf1b4876b04154990969")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mma", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
