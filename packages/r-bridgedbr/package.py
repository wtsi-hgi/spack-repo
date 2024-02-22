# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBridgedbr(RPackage):
	"""Code for using BridgeDb identifier mapping framework from within R

	Use BridgeDb functions and load identifier mapping databases in R. It uses GitHub, Zenodo, and Figshare if you use this package to download identifier mappings files.
	"""
	
	homepage = "https://github.com/bridgedb/BridgeDbR"
	bioc = "BridgeDbR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BridgeDbR_2.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BridgeDbR/BridgeDbR_2.12.0.tar.gz"]

	version("2.12.0", md5="2c155c28cb8d117e2dc1b69873b91d84")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
