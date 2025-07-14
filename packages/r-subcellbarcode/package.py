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

	version("1.24.0", commit="fd4fea39bbfbdd2b4f467f925621f34c3b16cf43")
	version("1.18.0", commit="dc1e986ef333fe818b2a734b1e79acf8685d2222")

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
