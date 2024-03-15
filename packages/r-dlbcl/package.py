# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlbcl(RPackage):
	"""Diffuse large B-cell lymphoma expression data

	This package provides additional expression data on diffuse large B-cell lymphomas for the BioNet package.
	"""
	
	homepage = "http://bionet.bioapps.biozentrum.uni-wuerzburg.de/"
	bioc = "DLBCL" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DLBCL_1.42.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DLBCL/DLBCL_1.42.2.tar.gz"]

	version("1.42.2", md5="9b03687d068351440a46898ad6814ed9")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))

	# experiment