# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgadem(RPackage):
	"""de novo motif discovery

	rGADEM is an efficient de novo motif discovery tool for large-scale genomic sequence data. It is an open-source R package, which is based on the GADEM software.
	"""
	
	bioc = "rGADEM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rGADEM_2.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rGADEM/rGADEM_2.50.0.tar.gz"]

	version("2.50.0", md5="17a121fa91f30cba09ed9dbb6b318555")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
