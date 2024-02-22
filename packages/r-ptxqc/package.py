# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtxqc(RPackage):
	"""Quality Report Generation for MaxQuant and mzTab Results

	Generates Proteomics (PTX) quality control (QC) reports for shotgun LC-MS data analyzed with the 
             MaxQuant software suite (from .txt files) or mzTab files (ideally from OpenMS 'QualityControl' tool).
             Reports are customizable (target thresholds, subsetting) and available in HTML or PDF format.
             Published in J. Proteome Res., Proteomics Quality Control: Quality Control Software for MaxQuant Results (2015)
             <doi:10.1021/acs.jproteome.5b00780>.
	"""
	
	homepage = "https://github.com/cbielow/PTXQC"
	cran = "PTXQC" 

	version("1.1.0", md5="42dd907fdebaaf2da7b029f620da81c0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-htmltable", type=("build", "run"))
	depends_on("r-knitr@1.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-r6p", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rmzqc@0.5:", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
