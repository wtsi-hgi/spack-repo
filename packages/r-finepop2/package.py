# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinepop2(RPackage):
	"""Fine-Scale Population Analysis (Rewrite for
Gene-Trait-Environment Interaction Analysis)

	Statistical tool set for population genetics. The package provides following functions: 1) estimators of genetic differentiation (FST), 2) regression analysis of environmental effects on genetic differentiation using generalized least squares (GLS) method, 3) interfaces to read and manipulate 'GENEPOP' format data files). For more information, see Kitada, Nakamichi and Kishino (2020) <doi:10.1101/2020.01.30.927186>.
	"""
	
	cran = "FinePop2" 

	version("0.4", md5="0f6ee7f1476891e9fec301725c5006db", url="https://cran.r-project.org/src/contrib/FinePop2_0.4.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))
