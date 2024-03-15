# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34bprobe(RPackage):
	"""Probe sequence data for microarrays of type rgu34b

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RG-U34B_probe_tab.
	"""
	
	bioc = "rgu34bprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34bprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34bprobe/rgu34bprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="2d6488309c5e54231a18e2ecf5608bb1")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation