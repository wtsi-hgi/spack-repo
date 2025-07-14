# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClumsid(RPackage):
	"""Clustering of MS2 Spectra for Metabolite Identification

	CluMSID is a tool that aids the identification of features in untargeted LC-MS/MS analysis by the use of MS2 spectra similarity and unsupervised statistical methods. It offers functions for a complete and customisable workflow from raw data to visualisations and is interfaceable with the xmcs family of preprocessing packages.
	"""
	
	homepage = "https://github.com/tdepke/CluMSID"
	bioc = "CluMSID"

	version("1.24.0", commit="4ebdb548a408fdabd88de20fbc8d5594d20d3ca7")
	version("1.18.0", commit="ce1d21e9582ad94315bd43f38b8ce8a66e8eec0c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mzr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
