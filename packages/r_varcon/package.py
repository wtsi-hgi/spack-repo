# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarcon(RPackage):
	"""VarCon: an R package for retrieving neighboring nucleotides of an SNV

	VarCon is an R package which converts the positional information from the annotation of an single nucleotide variation (SNV) (either referring to the coding sequence or the reference genomic sequence). It retrieves the genomic reference sequence around the position of the single nucleotide variation. To asses, whether the SNV could potentially influence binding of splicing regulatory proteins VarCon calcualtes the HEXplorer score as an estimation. Besides, VarCon additionally reports splice site strengths of splice sites within the retrieved genomic sequence and any changes due to the SNV.
	"""
	
	bioc = "VarCon" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/VarCon_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/VarCon/VarCon_1.10.0.tar.gz"]

	version("1.10.0", md5="843e95d7843d7611c222d8cbca8814b1")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
