# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvc1(RPackage):
	"""C-Statistics for Risk Prediction Models with Censored Survival
Data

	Performs inference for C of risk prediction models with censored survival data, using the method proposed by Uno et al. (2011) <doi:10.1002/sim.4154>. Inference for the difference in C between two competing prediction models is also implemented.
	"""
	
	cran = "survC1" 

	version("1.0-3", md5="57d5042eeb403d56440b0fcce61c0d8b", url="https://cran.r-project.org/src/contrib/survC1_1.0-3.tar.gz")

	depends_on("r-survival", type=("build", "run"))
