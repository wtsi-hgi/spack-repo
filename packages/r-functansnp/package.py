# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunctansnp(RPackage):
	"""Functional Analysis (with Interactions) for Dense SNP Data

	An implementation of revised functional regression models for multiple genetic variation data, such as single nucleotide polymorphism (SNP) data, which provides revised functional linear regression models, partially functional interaction regression analysis with penalty-based techniques and corresponding drawing functions, etc.(Ruzong Fan, Yifan Wang, James L. Mills, Alexander F. Wilson, Joan E. Bailey-Wilson, and Momiao Xiong (2013) <doi:10.1002/gepi.21757>).
	"""
	
	cran = "FunctanSNP" 

	version("0.1.0", md5="4dc7a1b2ac53cd2dced406448025134a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lava", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fundata", type=("build", "run"))
