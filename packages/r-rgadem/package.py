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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rGADEM_2.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rGADEM/rGADEM_2.50.0.tar.gz"]

	version("2.56.0", tag="RELEASE_3_21")
	version("2.50.0", sha256="f67e77b038aa1d56c261744d3467569ac6f5b9e6564a56253cc66e5316d64c92")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
