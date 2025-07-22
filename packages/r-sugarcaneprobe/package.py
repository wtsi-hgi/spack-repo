# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSugarcaneprobe(RPackage):
	"""Probe sequence data for microarrays of type sugarcane

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Sugar_Cane_probe_tab.
	"""
	
	bioc = "sugarcaneprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/sugarcaneprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/sugarcaneprobe/sugarcaneprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="300a7067194aec7a74fa76ee0ae8fba382a9d8a51d94735730f5b48e5af3f99f")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

