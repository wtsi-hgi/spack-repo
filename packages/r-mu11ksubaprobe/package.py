# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu11ksubaprobe(RPackage):
	"""Probe sequence data for microarrays of type mu11ksuba

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Mu11KsubA_probe_tab.
	"""
	
	bioc = "mu11ksubaprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mu11ksubaprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mu11ksubaprobe/mu11ksubaprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="813cd0750cca6ff0cfb696b83286177e")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation