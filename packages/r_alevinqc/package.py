# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlevinqc(RPackage):
	"""Generate QC Reports For Alevin Output

	Generate QC reports summarizing the output from an alevin, alevin-fry, or simpleaf run. Reports can be generated as html or pdf files, or as shiny applications.
	"""
	
	homepage = "https://github.com/csoneson/alevinQC"
	bioc = "alevinQC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/alevinQC_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/alevinQC/alevinQC_1.18.0.tar.gz"]

	version("1.18.0", md5="fa79ac8ac72e4d6d16c096886e9f759d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rmarkdown@2.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-tximport@1.17.4:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
