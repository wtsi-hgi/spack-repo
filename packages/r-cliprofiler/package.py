# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliprofiler(RPackage):
	"""A package for the CLIP data visualization

	An easy and fast way to visualize and profile the high-throughput IP data. This package generates the meta gene profile and other profiles. These profiles could provide valuable information for understanding the IP experiment results.
	"""
	
	homepage = "https://github.com/Codezy99/cliProfiler"
	bioc = "cliProfiler" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cliProfiler_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cliProfiler/cliProfiler_1.8.0.tar.gz"]

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="d4a72146a377bf0b36dd9b9891eb15fe5d111134dbd8c36a640990dd58f1677f")

	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
