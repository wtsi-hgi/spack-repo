# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsesa(RPackage):
	"""CRISPR-Based Salmonella Enterica Serotype Analyzer

	Salmonella enterica is a major cause of bacterial food-borne disease worldwide. Serotype identification is the most commonly used typing method to characterize Salmonella isolates. However, experimental serotyping needs great cost on manpower and resources. Recently, we found that the newly incorporated spacer in the clustered regularly interspaced short palindromic repeat (CRISPR) could serve as an effective marker for typing of Salmonella. It was further revealed by Li et. al (2014) <doi:10.1128/JCM.00696-14> that recognized types based on the combination of two newly incorporated spacer in both CRISPR loci showed high accordance with serotypes. Here, we developed an R package 'CSESA' to predict the serotype based on this finding. Considering it’s time saving and of high accuracy, we recommend to predict the serotypes of unknown Salmonella isolates using 'CSESA' before doing the traditional serotyping.
	"""
	
	cran = "CSESA" 

	version("1.2.0", md5="5079f1d304c60c764fb0f6eaaa9d15e4")

	depends_on("r-biostrings", type=("build", "run"))
