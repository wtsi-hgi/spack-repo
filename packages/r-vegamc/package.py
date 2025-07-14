# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegamc(RPackage):
	"""VegaMC: A Package Implementing a Variational Piecewise Smooth Model for Identification of Driver Chromosomal Imbalances in Cancer

	This package enables the detection of driver chromosomal imbalances including loss of heterozygosity (LOH) from array comparative genomic hybridization (aCGH) data. VegaMC performs a joint segmentation of a dataset and uses a statistical framework to distinguish between driver and passenger mutation. VegaMC has been implemented so that it can be immediately integrated with the output produced by PennCNV tool. In addition, VegaMC produces in output two web pages that allows a rapid navigation between both the detected regions and the altered genes. In the web page that summarizes the altered genes, the link to the respective Ensembl gene web page is reported.
	"""
	
	bioc = "VegaMC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/VegaMC_3.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/VegaMC/VegaMC_3.40.0.tar.gz"]

	version("3.46.0", tag="RELEASE_3_21")
	version("3.40.0", sha256="08605ff9b1a6e0f87a28226fc8c67f044aaea867bbe255943c4e6f25a7f83be9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
