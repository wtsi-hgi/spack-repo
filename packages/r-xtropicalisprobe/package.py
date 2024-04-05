# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtropicalisprobe(RPackage):
	"""Probe sequence data for microarrays of type xtropicalis

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was X_tropicalis_probe_tab.
	"""
	
	bioc = "xtropicalisprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/xtropicalisprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/xtropicalisprobe/xtropicalisprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="43d15a7e12edaec1bb5f24b87498b599")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

