# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylclock(RPackage):
	"""Methylclock - DNA methylation-based clocks

	This package allows to estimate chronological and gestational DNA methylation (DNAm) age as well as biological age using different methylation clocks. Chronological DNAm age (in years) : Horvath's clock, Hannum's clock, BNN, Horvath's skin+blood clock, PedBE clock and Wu's clock. Gestational DNAm age : Knight's clock, Bohlin's clock, Mayne's clock and Lee's clocks. Biological DNAm clocks : Levine's clock and Telomere Length's clock.
	"""
	
	homepage = "https://github.com/isglobal-brge/methylclock"
	bioc = "methylclock" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methylclock_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methylclock/methylclock_1.8.0.tar.gz"]

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="813248b3f4cabf05919de15147630e8290984f0bdce177de4445ed6683a85eda")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-methylclockdata", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rpmm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-planet", type=("build", "run"))
