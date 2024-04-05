# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAthalianaTair04232008(RPackage):
	"""Full genome sequences for Arabidopsis thaliana (TAIR version from April 23, 2008)

	Full genome sequences for Arabidopsis thaliana as provided by TAIR (snapshot from April 23, 2008) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Athaliana.TAIR.04232008" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Athaliana.TAIR.04232008_1.3.1000.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Athaliana.TAIR.04232008/BSgenome.Athaliana.TAIR.04232008_1.3.1000.tar.gz"]

	version("1.3.1000", md5="6b8a31a228dbcf4468974f5ec1d98467", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Athaliana.TAIR.04232008_1.3.1000.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

