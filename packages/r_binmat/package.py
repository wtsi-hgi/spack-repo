# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinmat(RPackage):
	"""Processes Binary Data Obtained from Fragment Analysis (Such as
AFLPs, ISSRs, and RFLPs)

	A molecular genetics tool that processes binary data from fragment analysis. It consolidates replicate sample pairs, outputs summary statistics, and produces hierarchical clustering trees and nMDS plots. This package was developed from the publication available here: <https://www.sciencedirect.com/science/article/pii/S1049964420306538>. The GUI version of this package is available on the R Shiny online server at: <https://clarkevansteenderen.shinyapps.io/BINMAT/> or it is accessible via GitHub by typing: shiny::runGitHub("BinMat", "clarkevansteenderen") into the console in R. Two real-world datasets accompany the package: an AFLP dataset of Bunias orientalis samples from Tewes et. al. (2017) <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/1365-2745.12869>, and an ISSR dataset of Nymphaea specimens from Reid et. al. (2021) <https://www.sciencedirect.com/science/article/pii/S0304377021000218> . The authors of these publications are thanked for allowing the use of their data.
	"""
	
	cran = "BinMat" 

	version("0.1.5", md5="820ff0efb94e6d1c19258f471e44f79a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pvclust@2:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.4:", type=("build", "run"))
