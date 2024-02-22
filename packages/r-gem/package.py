# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGem(RPackage):
	"""GEM: fast association study for the interplay of Gene, Environment and Methylation

	Tools for analyzing EWAS, methQTL and GxE genome widely.
	"""
	
	bioc = "GEM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GEM_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GEM/GEM_1.28.0.tar.gz"]

	version("1.28.0", md5="2c2c8e79fda151dee0060411c9610ff4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
