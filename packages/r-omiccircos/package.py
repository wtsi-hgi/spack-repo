# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmiccircos(RPackage):
	"""High-quality circular visualization of omics data

	OmicCircos is an R application and package for generating high-quality circular plots for omics data.
	"""
	
	bioc = "OmicCircos" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/OmicCircos_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/OmicCircos/OmicCircos_1.40.0.tar.gz"]

	version("1.40.0", md5="7d77b9a00853d3e6fec869012ce33daf")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
