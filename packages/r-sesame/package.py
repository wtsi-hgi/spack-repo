# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSesame(RPackage):
	"""SEnsible Step-wise Analysis of DNA MEthylation BeadChips

	Tools For analyzing Illumina Infinium DNA methylation arrays. SeSAMe provides utilities to support analyses of multiple generations of Infinium DNA methylation BeadChips, including preprocessing, quality control, visualization and inference. SeSAMe features accurate detection calling, intelligent inference of ethnicity, sex and advanced quality control routines.
	"""
	
	homepage = "https://github.com/zwdzwd/sesame"
	bioc = "sesame" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sesame_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sesame/sesame_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="b96ef69f13c55590d950ae1d2feb05ba478ed96595b782f39410df2175ae047a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sesamedata", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-wheatmap@0.2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
