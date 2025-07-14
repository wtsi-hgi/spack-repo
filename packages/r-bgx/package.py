# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgx(RPackage):
	"""Bayesian Gene eXpression

	Bayesian integrated analysis of Affymetrix GeneChips
	"""
	
	bioc = "bgx" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bgx_1.68.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bgx/bgx_1.68.3.tar.gz"]

	version("1.74.0", tag="RELEASE_3_21")
	version("1.68.3", sha256="570e86f5a75ab472dda41777d62e5e92b98211f2660934e76dc6f51aa2c070a8")

	depends_on("r@2.0.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy@1.5:", type=("build", "run"))
	depends_on("r-gcrma@2.4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("boost+random", type=("build", "link", "run"))
