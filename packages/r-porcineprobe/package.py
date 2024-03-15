# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPorcineprobe(RPackage):
	"""Probe sequence data for microarrays of type porcine

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Porcine_probe_tab.
	"""
	
	bioc = "porcineprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/porcineprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/porcineprobe/porcineprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="5ac483b6329a012d4c9954e3dee8869e")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation