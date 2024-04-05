# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133bprobe(RPackage):
	"""Probe sequence data for microarrays of type hgu133b

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U133B_probe_tab.
	"""
	
	bioc = "hgu133bprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133bprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133bprobe/hgu133bprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="203750510e51450e1267e08c241151c4")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

