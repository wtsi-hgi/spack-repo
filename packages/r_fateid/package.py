# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFateid(RPackage):
	"""Quantification of Fate Bias in Multipotent Progenitors

	Application of 'FateID' allows computation and visualization of cell fate bias for multi-lineage single cell transcriptome data. Herman, J.S., Sagar, Grün D. (2018) <DOI:10.1038/nmeth.4662>.
	"""
	
	cran = "FateID" 

	version("0.2.2", md5="d6e3864e72eca8379bca48d717c24045")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-som", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
