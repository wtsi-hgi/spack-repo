# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVivaldi(RPackage):
	"""Viral Variant Location and Diversity

	Analysis of minor alleles in Illumina sequencing data of viral
    genomes. Functions in 'vivaldi' primarily operate on vcf files.
	"""
	
	homepage = "https://github.com/GreshamLab/vivaldi"
	cran = "vivaldi" 

	version("1.0.1", md5="c7404ffaab7559991b46e412167b24a9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-plotly@4.10:", type=("build", "run"))
	depends_on("r-seqinr@4.2.8:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
	depends_on("r-vcfr@1.12:", type=("build", "run"))
