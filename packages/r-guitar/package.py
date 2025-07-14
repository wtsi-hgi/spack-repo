# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuitar(RPackage):
	"""Guitar

	The package is designed for visualization of RNA-related genomic features with respect to the landmarks of RNA transcripts, i.e., transcription starting site, start codon, stop codon and transcription ending site.
	"""
	
	bioc = "Guitar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Guitar_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Guitar/Guitar_2.18.0.tar.gz"]

	version("2.24.0", tag="RELEASE_3_21")
	version("2.18.0", sha256="cc56ce5145938591837b85e32651787641c0e110250993e04b6dffca1a922626")

	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
