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

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="16419352d21278d62543ff2de4be4fbc30575ef2feaa4812a488f9bf5556b603")

	depends_on("r@2.10:", type=("build", "run"))
