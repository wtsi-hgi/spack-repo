# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubcellbarcode(RPackage):
	"""SubCellBarCode: Integrated workflow for robust mapping and visualizing whole human spatial proteome

	Mass-Spectrometry based spatial proteomics have enabled the proteome-wide mapping of protein subcellular localization (Orre et al. 2019, Molecular Cell). SubCellBarCode R package robustly classifies proteins into corresponding subcellular localization.
	"""
	
	bioc = "SubCellBarCode" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SubCellBarCode_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SubCellBarCode/SubCellBarCode_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="83bb76a17d7e3844f00e0a78b1ae47decb8092997553b062c9b6d6d68faa4089")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
