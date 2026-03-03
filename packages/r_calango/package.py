# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalango(RPackage):
	"""Comparative Analysis with Annotation-Based Genomic Components

	A first-principle, phylogeny-aware comparative genomics tool for 
             investigating associations between terms used to annotate genomic
             components (e.g., Pfam IDs, Gene Ontology terms,) with quantitative 
             or rank variables such as number of cell types, genome size, or 
             density of specific genomic elements. See the project website for 
             more information, documentation and examples, and 
             <doi:10.1016/j.patter.2023.100728> for the full paper.
	"""
	
	homepage = "https://labpackages.github.io/CALANGO/"
	cran = "CALANGO" 

	version("1.0.16", md5="573bb330a8a98c312795e85e23d5f2aa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-pbmcapply@1.5:", type=("build", "run"))
	depends_on("r-ape@5.3:", type=("build", "run"))
	depends_on("r-rmarkdown@2.1:", type=("build", "run"))
	depends_on("r-nlme@3.1:", type=("build", "run"))
	depends_on("r-biocmanager@1.30.10:", type=("build", "run"))
	depends_on("r-taxize@0.9.92:", type=("build", "run"))
	depends_on("r-dendextend@1.15.2:", type=("build", "run"))
	depends_on("r-heatmaply@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.3.2:", type=("build", "run"))
	depends_on("r-plotly@4.9.2:", type=("build", "run"))
	depends_on("r-dt@0.13:", type=("build", "run"))
	depends_on("r-htmltools@0.5:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.1:", type=("build", "run"))
	depends_on("r-pkgdown@1.5.1:", type=("build", "run"))
	depends_on("r-knitr@1.28:", type=("build", "run"))
