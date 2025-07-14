# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMircomp(RPackage):
	"""Tools to assess and compare miRNA expression estimatation methods

	Based on a large miRNA dilution study, this package provides tools to read in the raw amplification data and use these data to assess the performance of methods that estimate expression from the amplification curves.
	"""
	
	bioc = "miRcomp" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/miRcomp_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/miRcomp/miRcomp_1.32.0.tar.gz"]

    version("1.38.1", tag="RELEASE_3_21")
	version("1.32.0", sha256="f54ee2b806f3da5ba09a1e0951ef2596ac22553a7717be8f7907ba7264af1713")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.22:", type=("build", "run"))
	depends_on("r-mircompdata", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
