# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMexplorer(RPackage):
	"""Identifying Master Gene Regulators from Gene Expression and
DNA-Binding Data

	The method 'm:Explorer' associates a given list of target genes (e.g. those involved in a biological process) to gene regulators such as transcription factors. Transcription factors that bind DNA near significantly many target genes or correlate with target genes in transcriptional (microarray or RNAseq data) are selected. Selection of candidate master regulators is carried out using multinomial regression models, likelihood ratio tests and multiple testing correction. Reference: m:Explorer: multinomial regression models reveal positive and negative regulators of longevity in yeast quiescence. Juri Reimand, Anu Aun, Jaak Vilo, Juan M Vaquerizas, Juhan Sedman and Nicholas M Luscombe. Genome Biology (2012) 13:R55 <doi:10.1186/gb-2012-13-6-r55>.
	"""
	
	cran = "mExplorer" 

	version("1.0.0", md5="3c421224ec47bdb6caf386cea1464ab1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-qusage", type=("build", "run"))
