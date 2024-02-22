# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsbig(RPackage):
	"""MSstats Preprocessing for Larger than Memory Data

	MSstats package provide tools for preprocessing, summarization and differential analysis of mass spectrometry (MS) proteomics data. Recently, some MS protocols enable acquisition of data sets that result in larger than memory quantitative data. MSstats functions are not able to process such data. MSstatsBig package provides additional converter functions that enable processing larger than memory data sets.
	"""
	
	bioc = "MSstatsBig" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MSstatsBig_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MSstatsBig/MSstatsBig_1.0.0.tar.gz"]

	version("1.0.0", md5="a53de589b47964296160c6fb8aaeb3b4")

	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-msstats", type=("build", "run"))
	depends_on("r-msstatsconvert", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sparklyr", type=("build", "run"))
