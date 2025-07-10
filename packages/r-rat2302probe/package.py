# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRat2302probe(RPackage):
	"""Probe sequence data for microarrays of type rat2302

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Rat230_2_probe_tab.
	"""
	
	bioc = "rat2302probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rat2302probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rat2302probe/rat2302probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="3b8872451c8e97d5e290c623a0f12b0b601a42475ffa18be5991b4b4d87a92ff")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

