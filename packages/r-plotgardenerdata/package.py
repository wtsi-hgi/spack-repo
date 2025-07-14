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

	version("1.14.0", commit="df1f4e9780ff2f6c9eaf7cfc42bd093fb0216136")
	version("1.8.0", commit="d513787280ad3ca35ed33d30f6dd8e7a0869ee19")

	depends_on("r@4.1:", type=("build", "run"))

