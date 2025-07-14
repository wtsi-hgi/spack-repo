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

	version("3.46.0", commit="d2f35f0ece6c7e3e28e53b8079a32365cf7afe74")
	version("3.40.0", commit="3f264cc443558a6437150bc2edcc26e2a05c5225")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
