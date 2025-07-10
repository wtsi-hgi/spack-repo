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

	version("1.42.2", sha256="4158ad04add57c96125eccfa9c4b9d0543f50bcd460c2a3bff3755f0fd92a41b")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))

