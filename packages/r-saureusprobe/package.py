# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaureusprobe(RPackage):
	"""Probe sequence data for microarrays of type saureus

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was S_aureus_probe_tab.
	"""
	
	bioc = "saureusprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/saureusprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/saureusprobe/saureusprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="eb4e91b10a536cbde4ecc08951ddf4d3")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation