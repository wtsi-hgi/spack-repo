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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CluMSID_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CluMSID/CluMSID_1.18.0.tar.gz"]

	version("1.18.0", sha256="fee61fb688e5e4dad9a42d75a81d14e6b1ee0757107c13162aef71be191bc547")

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
