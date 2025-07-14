# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsprep(RPackage):
	"""Package for Summarizing, Filtering, Imputing, and Normalizing Metabolomics Data

	Package performs summarization of replicates, filtering by frequency, several different options for imputing missing data, and a variety of options for transforming, batch correcting, and normalizing data.
	"""
	
	homepage = "https://github.com/KechrisLab/MSPrep"
	bioc = "MSPrep" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MSPrep_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MSPrep/MSPrep_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="11cae88a6c87effa217ae1c1cf6ca12b4ba9df07b3c694b51e6ad6a0b3de76b9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-pcamethods@1.24:", type=("build", "run"))
	depends_on("r-crmn", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
