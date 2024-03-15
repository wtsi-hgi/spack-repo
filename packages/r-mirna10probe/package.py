# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirna10probe(RPackage):
	"""Probe sequence data for microarrays of type mirna10

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was miRNA-1_0_probe_tab.
	"""
	
	bioc = "mirna10probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mirna10probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mirna10probe/mirna10probe_2.18.0.tar.gz"]

	version("2.18.0", md5="8bfa6cdfeee1c563b4881214bd5d4ce1")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation