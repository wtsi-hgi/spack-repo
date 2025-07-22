# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidashla(RPackage):
	"""R package for immunogenomics data handling and association analysis

	MiDAS is a R package for immunogenetics data transformation and statistical analysis. MiDAS accepts input data in the form of HLA alleles and KIR types, and can transform it into biologically meaningful variables, enabling HLA amino acid fine mapping, analyses of HLA evolutionary divergence, KIR gene presence, as well as validated HLA-KIR interactions. Further, it allows comprehensive statistical association analysis workflows with phenotypes of diverse measurement scales. MiDAS closes a gap between the inference of immunogenetic variation and its efficient utilization to make relevant discoveries related to T cell, Natural Killer cell, and disease biology.
	"""
	
	bioc = "midasHLA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/midasHLA_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/midasHLA/midasHLA_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="47e04642f640caa363d83809e675df26239efa43cc17e5cca6cfabfe990e2709")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-multiassayexperiment@1.8.3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-broom@0.5.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-formattable@0.2.0.1:", type=("build", "run"))
	depends_on("r-hardyweinberg@1.6.3:", type=("build", "run"))
	depends_on("r-kableextra@1.1:", type=("build", "run"))
	depends_on("r-knitr@1.21:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-stringi@1.2.4:", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.20.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.12:", type=("build", "run"))
	depends_on("r-tibble@2.0.1:", type=("build", "run"))
	depends_on("r-qdaptools@1.3.3:", type=("build", "run"))
