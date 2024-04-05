# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74cprobe(RPackage):
	"""Probe sequence data for microarrays of type mgu74c

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MG-U74C_probe_tab.
	"""
	
	bioc = "mgu74cprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74cprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74cprobe/mgu74cprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="186992992708f0071fd552ef92b9e25c")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

