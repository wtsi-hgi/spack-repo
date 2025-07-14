# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcplus(RPackage):
	"""Operating characteristics plus sample size and local fdr for microarray experiments

	This package allows to characterize the operating characteristics of a microarray experiment, i.e. the trade-off between false discovery rate and the power to detect truly regulated genes. The package includes tools both for planned experiments (for sample size assessment) and for already collected data (identification of differentially expressed genes).
	"""
	
	bioc = "OCplus"

	version("1.82.0", commit="abf71aa13a261623c46830a7085f54ab89e8e38a")
	version("1.76.0", commit="54692974caea38221dfb655641f05791e8b98fbc")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-multtest@1.7.3:", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
