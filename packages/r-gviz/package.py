# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGviz(RPackage):
	"""Plotting data and annotation information along genomic coordinates.

	Genomic data analyses requires integrated visualization of known genomic
	information and new experimental data. Gviz uses the biomaRt and the
	rtracklayer packages to perform live annotation queries to Ensembl and
	UCSC and translates this to e.g. gene/transcript structures in viewports
	of the grid graphics package. This results in genomic information
	plotted together with your data."""

	bioc = "Gviz"

	license("Artistic-2.0")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Gviz_1.46.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Gviz/Gviz_1.46.1.tar.gz"]

	version("1.46.1", md5="2e1eba2ac7cb0d1178f17bba471b0a62")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-iranges@1.99.18:", type=("build", "run"))
	depends_on("r-genomicranges@1.17.20:", type=("build", "run"))
	depends_on("r-xvector@0.5.7:", type=("build", "run"))
	depends_on("r-rtracklayer@1.25.13:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biomart@2.11:", type=("build", "run"))
	depends_on("r-annotationdbi@1.27.5:", type=("build", "run"))
	depends_on("r-biobase@2.15.3:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.17.22:", type=("build", "run"))
	depends_on("r-ensembldb@2.11.3:", type=("build", "run"))
	depends_on("r-bsgenome@1.33.1:", type=("build", "run"))
	depends_on("r-biostrings@2.33.11:", type=("build", "run"))
	depends_on("r-biovizbase@1.13.8:", type=("build", "run"))
	depends_on("r-rsamtools@1.17.28:", type=("build", "run"))
	depends_on("r-latticeextra@0.6.26:", type=("build", "run"))
	depends_on("r-matrixstats@0.8.14:", type=("build", "run"))
	depends_on("r-genomicalignments@1.1.16:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.1.3:", type=("build", "run"))
	depends_on("r-biocgenerics@0.11.3:", type=("build", "run"))
	depends_on("r-digest@0.6.8:", type=("build", "run"))
