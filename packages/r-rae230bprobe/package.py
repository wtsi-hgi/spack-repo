# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230bprobe(RPackage):
	"""Probe sequence data for microarrays of type rae230b

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RAE230B_probe_tab.
	"""
	
	bioc = "rae230bprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rae230bprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rae230bprobe/rae230bprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="7bdb3a07e1f00de8ff510a69bdac4c53")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation