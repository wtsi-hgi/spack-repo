# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitrusprobe(RPackage):
	"""Probe sequence data for microarrays of type citrus

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Citrus_probe_tab.
	"""
	
	bioc = "citrusprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/citrusprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/citrusprobe/citrusprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="259b114f96d5307c447d000bd27a7d15")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation