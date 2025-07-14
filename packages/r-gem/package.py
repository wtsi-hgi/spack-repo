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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GEM_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GEM/GEM_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="efbefb501dba47569251bb643ea4f8707c1e88f93e49500b80489934f095f0c3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
