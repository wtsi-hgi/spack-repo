# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanine2probe(RPackage):
	"""Probe sequence data for microarrays of type canine2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Canine_2_probe_tab.
	"""
	
	bioc = "canine2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/canine2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/canine2probe/canine2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="8bfc547c4677129e4f398403ed810331a0a710599b02dd35bb9378dc824a04d1")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

