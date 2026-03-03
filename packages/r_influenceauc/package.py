# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfluenceauc(RPackage):
	"""Identify Influential Observations in Binary Classification

	Ke, B. S., Chiang, A. J., & Chang, Y. C. I. (2018) <doi:10.1080/10543406.2017.1377728> provide two theoretical methods (influence function and local influence) based on the area under the receiver operating characteristic curve (AUC) to quantify the numerical impact of each observation to the overall AUC. Alternative graphical tools, cumulative lift charts, are proposed to reveal the existences and approximate locations of those influential observations through data visualization.
	"""
	
	cran = "influenceAUC" 

	version("0.1.2", md5="8ffbed0c21ed1f7114bed40cb825b1ab")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
