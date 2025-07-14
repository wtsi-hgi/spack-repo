# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetsam(RPackage):
	"""Network Seriation And Modularization

	The NetSAM (Network Seriation and Modularization) package takes an edge-list representation of a weighted or unweighted network as an input, performs network seriation and modularization analysis, and generates as files that can be used as an input for the one-dimensional network visualization tool NetGestalt (http://www.netgestalt.org) or other network analysis. The NetSAM package can also generate correlation network (e.g. co-expression network) based on the input matrix data, perform seriation and modularization analysis for the correlation network and calculate the associations between the sample features and modules or identify the associated GO terms for the modules.
	"""
	
	bioc = "NetSAM" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NetSAM_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NetSAM/NetSAM_1.42.0.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="8a22967f7a745e5accc3ca92a6ff7e3e1caa45d6141e82ee2ab78180ef1933f9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-seriation@1.0.6:", type=("build", "run"))
	depends_on("r-igraph@0.6.1:", type=("build", "run"))
	depends_on("r-wgcna@1.34:", type=("build", "run"))
	depends_on("r-biomart@2.18:", type=("build", "run"))
	depends_on("r-annotationdbi@1.28:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4:", type=("build", "run"))
	depends_on("r-survival@2.37.7:", type=("build", "run"))
	depends_on("r-go-db@2.10:", type=("build", "run"))
	depends_on("r-r2html@2.2:", type=("build", "run"))
	depends_on("r-dbi@0.5.1:", type=("build", "run"))
