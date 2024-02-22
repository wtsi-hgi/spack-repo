# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaeg1aprobe(RPackage):
	"""Probe sequence data for microarrays of type paeg1a

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was P_aeg1a_probe_tab.
	"""
	
	bioc = "paeg1aprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/paeg1aprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/paeg1aprobe/paeg1aprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="493fa1fc7b92a78c8114b65038113c42")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation