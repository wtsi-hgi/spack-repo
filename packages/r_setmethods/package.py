# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSetmethods(RPackage):
	"""Functions for Set-Theoretic Multi-Method Research and Advanced
QCA

	Functions for performing set-theoretic multi-method research, QCA for clustered data, theory evaluation, Enhanced Standard Analysis, indirect calibration, radar visualisations. Additionally it includes data to replicate the 	examples in the books by Oana, I.E, C. Q. Schneider, and E. Thomann. Qualitative Comparative Analysis (QCA) using R: A Beginner's Guide. Cambridge University Press and C. Q. Schneider and C. Wagemann "Set Theoretic Methods for the Social Sciences", Cambridge University Press.
	"""
	
	cran = "SetMethods" 

	version("4.0", md5="1e272704a0bbc0404147bd520678f248")

	depends_on("r-qca", type=("build", "run"))
	depends_on("r-admisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-stargazer", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
