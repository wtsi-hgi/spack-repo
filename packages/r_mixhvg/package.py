# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixhvg(RPackage):
	"""Mixture of Multiple Highly Variable Feature Selection Methods

	Highly variable gene selection methods, including popular public available methods, and also the mixture of multiple highly variable gene selection methods, <https://github.com/RuzhangZhao/mixhvg>.
	"""
	
	cran = "mixhvg" 

	version("0.1.1", md5="4502de2e233eb7039260e95b151389cb")

	depends_on("r-scran", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
