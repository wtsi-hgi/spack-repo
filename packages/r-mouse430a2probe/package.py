# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse430a2probe(RPackage):
	"""Probe sequence data for microarrays of type mouse430a2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Mouse430A_2_probe_tab.
	"""
	
	bioc = "mouse430a2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse430a2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse430a2probe/mouse430a2probe_2.18.0.tar.gz"]

	version("2.18.0", md5="bb3c34477d4fcf03a539772011118795")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation