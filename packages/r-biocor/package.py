# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocor(RPackage):
	"""Functional similarities

	Calculates functional similarities based on the pathways described on KEGG and REACTOME or in gene sets. These similarities can be calculated for pathways or gene sets, genes, or clusters and combined with other similarities. They can be used to improve networks, gene selection, testing relationships...
	"""
	
	homepage = "https://bioconductor.org/packages/BioCor"
	bioc = "BioCor" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioCor_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioCor/BioCor_1.26.0.tar.gz"]

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="341a2a3a57eca622b5e166f209623adaccfd6179b08d5ba303a96858006d201c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
