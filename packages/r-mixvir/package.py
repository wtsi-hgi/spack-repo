# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixvir(RPackage):
	"""Analysis and Exploration of Mixed Microbial Genomic Samples

	Tool for exploring DNA and amino acid variation and inferring the presence of target lineages from microbial high-throughput genomic DNA samples that potentially contain mixtures of variants/lineages. MixviR was originally created to help analyze environmental SARS-CoV-2/Covid-19 samples from environmental sources such as wastewater or dust, but can be applied to any microbial group. Inputs include reference genome information in commonly-used file formats (fasta, bed) and one or more variant call format (VCF) files, which can be generated with programs such as Illumina's DRAGEN, the Genome Analysis Toolkit, or bcftools. See DePristo et al (2011) <doi:10.1038/ng.806> and Danecek et al (2021) <doi:10.1093/gigascience/giab008> for these tools, respectively. Available outputs include a table of mutations observed in the sample(s), estimates of proportions of target lineages in the sample(s), and an R Shiny dashboard to interactively explore the data. 
	"""
	
	homepage = "https://github.com/mikesovic/MixviR"
	cran = "MixviR" 

	version("3.5.0", md5="73ca29348af440116968abe408f62c7f")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly@4.9.4:", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr@1.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-vcfr@1.11:", type=("build", "run"))
