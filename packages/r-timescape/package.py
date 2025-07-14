# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimescape(RPackage):
	"""Patient Clonal Timescapes

	TimeScape is an automated tool for navigating temporal clonal evolution data. The key attributes of this implementation involve the enumeration of clones, their evolutionary relationships and their shifting dynamics over time. TimeScape requires two inputs: (i) the clonal phylogeny and (ii) the clonal prevalences. Optionally, TimeScape accepts a data table of targeted mutations observed in each clone and their allele prevalences over time. The output is the TimeScape plot showing clonal prevalence vertically, time horizontally, and the plot height optionally encoding tumour volume during tumour-shrinking events. At each sampling time point (denoted by a faint white line), the height of each clone accurately reflects its proportionate prevalence. These prevalences form the anchors for bezier curves that visually represent the dynamic transitions between time points.
	"""
	
	bioc = "timescape" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/timescape_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/timescape/timescape_1.26.0.tar.gz"]

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="be100e9db81353fcbe7061d656e4a31d1b196deb10bb98277f068806fab263f9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.5:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
