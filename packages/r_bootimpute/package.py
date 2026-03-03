# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootimpute(RPackage):
	"""Bootstrap Inference for Multiple Imputation

	Bootstraps and imputes incomplete datasets. Then performs inference on estimates obtained from analysing the imputed datasets as proposed by von Hippel and Bartlett (2021) <doi:10.1214/20-STS793>.
	"""
	
	cran = "bootImpute" 

	version("1.2.1", md5="2178ce9fb6117da9a0868528d198efed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-smcfcs", type=("build", "run"))
