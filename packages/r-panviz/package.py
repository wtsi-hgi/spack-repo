# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanviz(RPackage):
	"""Integrating Multi-Omic Network Data With Summay-Level GWAS Data

	This pacakge integrates data from the Kyoto Encyclopedia of Genes and Genomes (KEGG) with summary-level genome-wide association (GWAS) data, such as that provided by the GWAS Catalog or GWAS Central databases, or a user's own study or dataset, in order to produce biological networks, termed IMONs (Integrated Multi-Omic Networks). IMONs can be used to analyse trait-specific polymorphic data within the context of biochemical and metabolic reaction networks, providing greater biological interpretability for GWAS data.
	"""
	
	homepage = "https://github.com/LucaAnholt/PanViz"
	bioc = "PanViz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PanViz_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PanViz/PanViz_1.4.0.tar.gz"]

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="a05161ea6299e1426430c604c4e6ce050aa4b528b8d32c32f5fe43d8522b52a5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-easycsv", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
