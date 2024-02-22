# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpimage(RPackage):
	"""Tool For Analysis of Images in Experiments

	Tools created for image analysis in researches. There are functions associated with image editing, segmentation, and obtaining biometric measurements (Este pacote foi idealizado para para a analise de imagens em pesquisas. Ha funcoes associadas a edicao de imagens, segmentacao, e obtencao de medidas biometricas).
	"""
	
	homepage = "https://www.youtube.com/channel/UCDGyvLCJnv9RtTY1YMBMVNQ"
	cran = "ExpImage" 

	version("0.9.0", md5="6affd440a870538255b5014317b3cc91")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-schemr", type=("build", "run"))
