# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransreg(RPackage):
	"""Penalised Regression with Multiple Sets of Prior Effects

	Improves the predictive performance of ridge and lasso regression exploiting one or more sources of prior information on the importance and direction of effects (Rauschenberger and others 2023, <doi:10.1093/bioinformatics/btad680>). For running the vignette, install 'fwelnet' from 'GitHub' <https://github.com/kjytay/fwelnet>.
	"""
	
	homepage = "https://lcsb-bds.github.io/transreg/"
	cran = "transreg" 

	version("1.0.2", md5="9a263bd8d0b74da2d3005b51cd9029fc")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-starnet", type=("build", "run"))
	depends_on("r-joinet", type=("build", "run"))
