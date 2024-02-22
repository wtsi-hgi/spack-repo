# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocuszoomr(RPackage):
	"""Gene Locus Plot with Gene Annotations

	Publication-ready regional gene locus plots similar to those produced by the web interface 'LocusZoom' <https://my.locuszoom.org>, but running locally in R. Genetic or genomic data with gene annotation tracks are plotted via R base graphics, 'ggplot2' or 'plotly', allowing flexibility and easy customisation including laying out multiple locus plots on the same page. It uses the 'LDlink' API <https://ldlink.nih.gov/?tab=apiaccess> to query linkage disequilibrium data from the 1000 Genomes Project and can overlay this on plots.
	"""
	
	homepage = "https://github.com/myles-lewis/locuszoomr"
	cran = "locuszoomr" 

	version("0.2.1", md5="9ab5bc1926b958569486d6a1a1158379")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gggrid", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ldlinkr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
