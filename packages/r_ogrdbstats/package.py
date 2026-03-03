# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROgrdbstats(RPackage):
	"""Analysis of Adaptive Immune Receptor Repertoire Germ Line
Statistics

	Multiple tools are now available for inferring the personalised 
    germ line set from an adaptive immune receptor repertoire. 
    Output from these tools is converted to 
    a single format and supplemented with rich data such as usage and 
    characterisation of 'novel' germ line alleles. This data can be 
    particularly useful when considering the validity of novel inferences. Use
    of the analysis provided is described in <doi:10.3389/fimmu.2019.00435>.
	"""
	
	homepage = "https://github.com/airr-community/ogrdbstats"
	cran = "ogrdbstats" 

	version("0.5.0", md5="432da9151421542d33dde656ba46a2fe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tigger@0.4:", type=("build", "run"))
	depends_on("r-alakazam@0.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringdist@0.9.5.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-biostrings@2.52:", type=("build", "run"))
	depends_on("r-argparser@0.4:", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
