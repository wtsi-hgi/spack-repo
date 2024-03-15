# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosia(RPackage):
	"""An Investigation Across Different Species and Tissues

	Cross-Species Investigation and Analysis (CoSIA) is a package that provides researchers with an alternative methodology for comparing across species and tissues using normal wild-type RNA-Seq Gene Expression data from Bgee. Using RNA-Seq Gene Expression data, CoSIA provides multiple visualization tools to explore the transcriptome diversity and variation across genes, tissues, and species. CoSIA uses the Coefficient of Variation and Shannon Entropy and Specificity to calculate transcriptome diversity and variation. CoSIA also provides additional conversion tools and utilities to provide a streamlined methodology for cross-species comparison.
	"""
	
	homepage = "https://www.lasseigne.org/"
	bioc = "CoSIA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CoSIA_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CoSIA/CoSIA_1.2.0.tar.gz"]

	version("1.2.0", md5="217ff53ed0aac2ca3c2d91ce5237c111")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-experimenthub@2.7:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-plotly@4.10:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.12:", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.12:", type=("build", "run"))
	depends_on("r-org-dr-eg-db@3.12:", type=("build", "run"))
	depends_on("r-org-ce-eg-db@3.12:", type=("build", "run"))
	depends_on("r-org-dm-eg-db@3.12:", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.12:", type=("build", "run"))
	depends_on("r-annotationdbi@1.52:", type=("build", "run"))
	depends_on("r-biomart@2.46.3:", type=("build", "run"))
	depends_on("r-homologene@1.4.68.19:", type=("build", "run"))
	depends_on("r-annotationtools@1.64:", type=("build", "run"))
	depends_on("r-readr@2.1.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
