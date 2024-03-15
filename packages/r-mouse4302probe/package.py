# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse4302probe(RPackage):
	"""Probe sequence data for microarrays of type mouse4302

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Mouse430_2_probe_tab.
	"""
	
	bioc = "mouse4302probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse4302probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse4302probe/mouse4302probe_2.18.0.tar.gz"]

	version("2.18.0", md5="7116787a7db241a545e79e419a8cfa0d")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation