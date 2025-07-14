# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbh(RPackage):
	"""Interaction Based Homogeneity for Evaluating Gene Lists

	This package contains methods for calculating Interaction Based Homogeneity to evaluate fitness of gene lists to an interaction network which is useful for evaluation of clustering results and gene list analysis. BioGRID interactions are used in the calculation. The user can also provide their own interactions.
	"""
	
	bioc = "ibh" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ibh_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ibh/ibh_1.50.0.tar.gz"]

	version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="6dda7c7d35077d27f72033179035863ea7b00d9140ee11e7357cb22ef279f7ca")

	depends_on("r-simpintlists", type=("build", "run"))
