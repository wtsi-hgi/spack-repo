# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhybridfinder(RPackage):
	"""Identification of Hybrid Peptides in Immunopeptidomic Analyses

	Tool for the analysis Mass Spectrometry (MS) data in the context of 
             immunopeptidomic analysis for the identification of hybrid 
             peptides and the predictions of binding affinity of all peptides 
             using 'netMHCpan' <doi:10.1093/nar/gkaa379> while providing a summary 
             of the netMHCpan output. 'RHybridFinder' (RHF) is destined for 
             researchers who are looking to analyze their MS data for the purpose 
             of identification of potential spliced peptides. This package, 
             developed mainly in base R, is based on the workflow published by 
             Faridi et al. in 2018 <doi:10.1126/sciimmunol.aar3947>.
	"""
	
	cran = "RHybridFinder" 

	version("0.2.0", md5="ab0696d08ea1bda7227cb436a18eb1a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
