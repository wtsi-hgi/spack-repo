# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReportingtools(RPackage):
	"""Tools for making reports in various formats.

	The ReportingTools software package enables users to easily display
	reports of analysis results generated from sources such as microarray
	and sequencing data. The package allows users to create HTML pages that
	may be viewed on a web browser such as Safari, or in other formats
	readable by programs such as Excel. Users can generate tables with
	sortable and filterable columns, make and display plots, and link table
	entries to other data sources such as NCBI or larger plots within the
	HTML page. Using the package, users can also produce a table of contents
	page to link various reports together for a particular project that can
	be viewed in a web browser. For more examples, please visit our site:
	http:// research-pub.gene.com/ReportingTools."""

	bioc = "ReportingTools"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ReportingTools_2.42.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ReportingTools/ReportingTools_2.42.3.tar.gz"]

	version("2.42.3", md5="71afa63c0311b91a64a17d476a16eb44")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-category", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-limma@3.17.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-pfam-db", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-biocgenerics@0.1.6:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-deseq2@1.3.41:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
