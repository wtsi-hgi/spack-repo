# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacorrplot(RPackage):
	"""Visualize artificial correlation in microarray data

	Graphically displays correlation in microarray data that is due to insufficient normalization
	"""
	
	homepage = "http://www.pubmedcentral.gov/articlerender.fcgi?tool=pubmed&pubmedid=15799785"
	bioc = "maCorrPlot" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/maCorrPlot_1.72.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/maCorrPlot/maCorrPlot_1.72.0.tar.gz"]

	version("1.72.0", md5="4d4be51b04e4ff3e09aff6643eeed215")

	depends_on("r-lattice", type=("build", "run"))
