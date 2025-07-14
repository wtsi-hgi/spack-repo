# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAracneNetworks(RPackage):
	"""ARACNe-inferred gene networks from TCGA tumor datasets

	This package contains ARACNe-inferred networks from TCGA tumor datasets. It also contains a function to export them into plain-text format.
	"""
	
	bioc = "aracne.networks" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/aracne.networks_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/aracne.networks/aracne.networks_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="6edb41a88287143eab8d8f7ac5c2877919a40ccc3468e1a4f5f300ff603afe99")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-viper", type=("build", "run"))

