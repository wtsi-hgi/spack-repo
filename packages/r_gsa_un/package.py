# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsaUn(RPackage):
	"""Global Sensitivity Analysis Tool

	A tool to sensitivity analysis using SOBOL (Sobol, 1993) and AMA (Dell'Oca et al. 2017 <doi:10.5194/hess-21-6219-2017>) indices.
            It allows to identify the most sensitive parameter or parameters of a model.
	"""
	
	cran = "GSA.UN" 

	version("1.0.0", md5="945954033a7c0a92375141a061b79c51")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
