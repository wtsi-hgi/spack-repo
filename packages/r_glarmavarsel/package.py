# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlarmavarsel(RPackage):
	"""Variable Selection in Sparse GLARMA Models

	Performs variable selection in high-dimensional sparse GLARMA models. For further details we refer the reader to the paper Gomtsyan et al. (2020), <arXiv:2007.08623v1>.
	"""
	
	cran = "GlarmaVarSel" 

	version("1.0", md5="2e2447a6f1c13899efecdd356de72adb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
