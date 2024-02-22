# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimeviewprobe(RPackage):
	"""Probe sequence data for microarrays of type primeview

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was PrimeView_probe_tab.
	"""
	
	bioc = "primeviewprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/primeviewprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/primeviewprobe/primeviewprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="87cc56a8da4fb742ab1558ce1d3d26cc")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation