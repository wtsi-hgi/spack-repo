# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPureseqtmr(RPackage):
	"""Predict Transmembrane Protein Topology

	Proteins reside in either the cell plasma or in the
    cell membrane. A membrane protein goes through the 
    membrane at least once. Given the amino acid sequence of a
    membrane protein, the tool
    'PureseqTM' (<https://github.com/PureseqTM/pureseqTM_package>,
    as described in "Efficient And Accurate Prediction Of Transmembrane 
    Topology From Amino acid sequence only.", Wang, Qing, et al (2019), 
    <doi:10.1101/627307>),
    can predict the topology of a membrane protein. This package
    allows one to use 'PureseqTM' from R.
	"""
	
	homepage = "https://github.com/richelbilderbeek/pureseqtmr/"
	cran = "pureseqtmr" 

	version("1.4", md5="9bb24de7b9ba461642c9505c35c3a0a1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-peptides", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
