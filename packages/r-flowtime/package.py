# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowtime(RPackage):
	"""Annotation and analysis of biological dynamical systems using flow cytometry

	This package facilitates analysis of both timecourse and steady state flow cytometry experiments. This package was originially developed for quantifying the function of gene regulatory networks in yeast (strain W303) expressing fluorescent reporter proteins using BD Accuri C6 and SORP cytometers. However, the functions are for the most part general and may be adapted for analysis of other organisms using other flow cytometers. Functions in this package facilitate the annotation of flow cytometry data with experimental metadata, as often required for publication and general ease-of-reuse. Functions for creating, saving and loading gate sets are also included. In the past, we have typically generated summary statistics for each flowset for each timepoint and then annotated and analyzed these summary statistics. This method loses a great deal of the power that comes from the large amounts of individual cell data generated in flow cytometry, by essentially collapsing this data into a bulk measurement after subsetting. In addition to these summary functions, this package also contains functions to facilitate annotation and analysis of steady-state or time-lapse data utilizing all of the data collected from the thousands of individual cells in each sample.
	"""
	
	bioc = "flowTime" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowTime_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowTime/flowTime_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="d28bae15c268b869ea81effb2974560bbb7bffe3a8885dc0e621f41e6b41e88c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
