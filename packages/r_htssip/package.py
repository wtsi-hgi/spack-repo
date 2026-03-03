# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtssip(RPackage):
	"""High Throughput Sequencing of Stable Isotope Probing Data
Analysis

	Functions for analyzing high throughput sequencing 
    stable isotope probing (HTS-SIP) data.
    Analyses include high resolution stable isotope probing (HR-SIP),
    multi-window high resolution stable isotope probing (MW-HR-SIP), 
    and quantitative stable isotope probing (q-SIP). 
	"""
	
	cran = "HTSSIP" 

	version("1.4.1", md5="3d815294310e64339f04b234263771d3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph@1.1.2:", type=("build", "run"))
	depends_on("r-ape@4.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-tidyr@0.7.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-vegan@2.4:", type=("build", "run"))
	depends_on("r-deseq2@1.16.1:", type=("build", "run"))
	depends_on("r-phyloseq@1.20:", type=("build", "run"))
	depends_on("r-coenocliner@0.2.2:", type=("build", "run"))
	depends_on("r-lazyeval@0.2:", type=("build", "run"))
