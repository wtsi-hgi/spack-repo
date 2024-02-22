# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmMulti(RPackage):
	"""Fit, Simulate and Diagnose Exponential-Family Models for
Multiple or Multilayer Networks

	A set of extensions for the 'ergm' package to fit multilayer/multiplex/multirelational networks and samples of multiple networks. 'ergm.multi' is a part of the Statnet suite of packages for network analysis. See Krivitsky, Koehly, and Marcum (2020) <doi:10.1007/s11336-020-09720-7> and Krivitsky, Coletti, and Hens (2023) <doi:10.1080/01621459.2023.2242627>.
	"""
	
	homepage = "https://statnet.org"
	cran = "ergm.multi" 

	version("0.2.1", md5="f17447659708913114c8b4a5d8cbea88")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-network@1.18.2:", type=("build", "run"))
	depends_on("r-statnet-common@4.9:", type=("build", "run"))
	depends_on("r-rlang@1.1.3:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-glue@1.7:", type=("build", "run"))
	depends_on("r-rle@0.9.2:", type=("build", "run"))
	depends_on("r-rdpack@2.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
