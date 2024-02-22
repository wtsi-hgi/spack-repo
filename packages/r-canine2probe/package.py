# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanine2probe(RPackage):
	"""Probe sequence data for microarrays of type canine2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Canine_2_probe_tab.
	"""
	
	bioc = "canine2probe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/canine2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/canine2probe/canine2probe_2.18.0.tar.gz"]

	version("2.18.0", md5="7de0f4ea616e8662dc2eaa9ab78d1f13")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation