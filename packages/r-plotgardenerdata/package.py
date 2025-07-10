# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotgardenerdata(RPackage):
	"""Datasets and test data files for the plotgardener package

	This is a supplemental data package for the plotgardener package. Includes example datasets used in plotgardener vignettes and example raw data files. For details on how to use these datasets, see the plotgardener package vignettes.
	"""
	
	homepage = "https://github.com/PhanstielLab/plotgardenerData"
	bioc = "plotgardenerData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/plotgardenerData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/plotgardenerData/plotgardenerData_1.8.0.tar.gz"]

	version("1.8.0", sha256="23d344e1aba587ac4a1ee22c9143a8f3b088e9eea7f4c37ca6a1e359260100b1")

	depends_on("r@4.1:", type=("build", "run"))

