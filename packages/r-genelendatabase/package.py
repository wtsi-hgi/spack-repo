# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenelendatabase(RPackage):
	"""Lengths of mRNA transcripts for a number of genomes.

	Length of mRNA transcripts for a number of genomes and gene ID formats,
	largely based on UCSC table browser"""

	bioc = "geneLenDataBase"
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/geneLenDataBase_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/geneLenDataBase/geneLenDataBase_1.38.0.tar.gz"]

	version("1.38.0", md5="c29099d3142aad07590e22ce37c6acf3")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicfeatures@1.3.15:", type=("build", "run"))

	# experiment