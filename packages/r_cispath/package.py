# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCispath(RPackage):
	"""Visualization and management of the protein-protein interaction networks.

	cisPath is an R package that uses web browsers to visualize and manage protein-protein interaction networks.
	"""
	
	bioc = "cisPath" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cisPath_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cisPath/cisPath_1.42.0.tar.gz"]

	version("1.42.0", md5="958a35281b9aa98b2d5c3a5c4e9c8824")

	depends_on("r@2.10:", type=("build", "run"))
