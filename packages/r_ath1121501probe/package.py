# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAth1121501probe(RPackage):
	"""Probe sequence data for microarrays of type ath1121501

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was ATH1-121501_probe_tab.
	"""
	
	bioc = "ath1121501probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ath1121501probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ath1121501probe/ath1121501probe_2.18.0.tar.gz"]

	version("2.18.0", md5="eeeae5e6550bb472ba3419d71bbd7dfb")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

