# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNacho(RPackage):
	"""NanoString Quality Control Dashboard

	NanoString nCounter data are gene expression assays
    where there is no need for the use of enzymes or amplification
    protocols and work with fluorescent barcodes (Geiss et al. (2018)
    <doi:10.1038/nbt1385>). Each barcode is assigned a
    messenger-RNA/micro-RNA (mRNA/miRNA) which after bonding with its
    target can be counted. As a result each count of a specific barcode
    represents the presence of its target mRNA/miRNA. 'NACHO' (NAnoString
    quality Control dasHbOard) is able to analyse the exported NanoString
    nCounter data and facilitates the user in performing a quality
    control. 'NACHO' does this by visualising quality control metrics,
    expression of control genes, principal components and sample specific
    size factors in an interactive web application.
	"""
	
	homepage = "https://github.com/mcanouil/NACHO/"
	cran = "NACHO" 

	version("2.0.6", md5="3468f125574a283984ea9f47f988ecc6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggforce@0.3.1:", type=("build", "run"))
	depends_on("r-ggrepel@0.8.1:", type=("build", "run"))
	depends_on("r-knitr@1.25:", type=("build", "run"))
	depends_on("r-rmarkdown@1.16:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinywidgets@0.4.9:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
