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
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rat2302probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rat2302probe/rat2302probe_2.18.0.tar.gz"]

	version("2.18.0", md5="d1d9215e52b9e845cc4d7c902536e0d6")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation