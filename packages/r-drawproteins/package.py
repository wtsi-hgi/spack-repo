# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrawproteins(RPackage):
	"""Package to Draw Protein Schematics from Uniprot API output

	This package draws protein schematics from Uniprot API output. From the JSON returned by the GET command, it creates a dataframe from the Uniprot Features API. This dataframe can then be used by geoms based on ggplot2 and base R to draw protein schematics.
	"""
	
	homepage = "https://github.com/brennanpincardiff/drawProteins"
	bioc = "drawProteins" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/drawProteins_1.22.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/drawProteins/drawProteins_1.22.2.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.2", sha256="7112a4924a43d9a0bb27ace07566dfbb97b30c44784d3553f3157e9d489088d5")
	version("1.22.0", md5="67cbf634b37851946e9cc3885cdda6c5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
