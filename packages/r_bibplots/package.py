# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBibplots(RPackage):
	"""Plot Functions for Use in Bibliometrics

	Currently, the package provides several functions for plotting and analyzing bibliometric data (JIF, Journal Impact Factor, and paper percentile values), beamplots with citations and percentiles, and three plot functions to visualize the result of a reference publication year spectroscopy (RPYS) analysis performed in the free software 'CRExplorer' (see <http://crexplorer.net>). Further extension to more plot variants is planned.
	"""
	
	cran = "BibPlots" 

	version("0.0.8", md5="26504e6f6798f6b390e4d9a6b923ea81")

	depends_on("r@3.1.2:", type=("build", "run"))
