# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiglarmavarsel(RPackage):
	"""Variable Selection in Sparse Multivariate GLARMA Models

	Performs variable selection in high-dimensional sparse GLARMA models. For further details we refer the reader to the paper Gomtsyan et al. (2022), <arXiv:2208.14721>.
	"""
	
	cran = "MultiGlarmaVarSel" 

	version("1.0", md5="430486a5ec66f1d22c50fba9288721ca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
