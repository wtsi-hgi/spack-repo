# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPfamanalyzer(RPackage):
	"""Identification of domain isotypes in pfam data

	Protein domains is one of the most import annoation of proteins we have with the Pfam database/tool being (by far) the most used tool. This R package enables the user to read the pfam prediction from both webserver and stand-alone runs into R. We have recently shown most human protein domains exist as multiple distinct variants termed domain isotypes. Different domain isotypes are used in a cell, tissue, and disease-specific manner. Accordingly, we find that domain isotypes, compared to each other, modulate, or abolish the functionality of a protein domain. This R package enables the identification and classification of such domain isotypes from Pfam data.
	"""
	
	bioc = "pfamAnalyzeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pfamAnalyzeR_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pfamAnalyzeR/pfamAnalyzeR_1.2.0.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="c7f89b30e3613df2a814fcfbd64c69d1d786da228cbf1a0ec1692deee6b9bd63")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
