# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNugohs1a520180probe(RPackage):
	"""Probe sequence data for microarrays of type nugohs1a520180

	This package was automatically created by package AnnotationForge version 1.11.20. The probe sequence data was obtained from http://www.affymetrix.com.
	"""
	
	bioc = "nugohs1a520180probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/nugohs1a520180probe_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/nugohs1a520180probe/nugohs1a520180probe_3.4.0.tar.gz"]

	version("3.4.0", md5="6acf20ac4a799eaae97d0a64426d6ac3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.20:", type=("build", "run"))

	# annotation