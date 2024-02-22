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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/miRcomp_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/miRcomp/miRcomp_1.32.0.tar.gz"]

	version("1.32.0", md5="06b97d8829ca13b60dd4869a48b684ab")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.22:", type=("build", "run"))
	depends_on("r-mircompdata", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
