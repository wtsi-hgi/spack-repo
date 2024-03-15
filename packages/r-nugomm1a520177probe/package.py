# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNugomm1a520177probe(RPackage):
	"""Probe sequence data for microarrays of type nugomm1a520177

	This package was automatically created by package AnnotationForge version 1.11.20. The probe sequence data was obtained from http://www.affymetrix.com.
	"""
	
	bioc = "nugomm1a520177probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/nugomm1a520177probe_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/nugomm1a520177probe/nugomm1a520177probe_3.4.0.tar.gz"]

	version("3.4.0", md5="7fa974389ad2be6ebda8810496221a9b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.20:", type=("build", "run"))

	# annotation