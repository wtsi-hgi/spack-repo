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

	version("1.48.0", commit="ded54bf8eb669e56ce88bf2dda06ec7a4fbb8986")
	version("1.42.0", commit="596bfc61d920c1b66e1a9fc83616b1b52202aa44")

	depends_on("r@2.10:", type=("build", "run"))
