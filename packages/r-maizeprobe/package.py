# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaizeprobe(RPackage):
	"""Probe sequence data for microarrays of type maize

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Maize_probe_tab.
	"""
	
	bioc = "maizeprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/maizeprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/maizeprobe/maizeprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="606a8c524b2c805877c937e7fbb20e9b6b9e7cbf31c538e1a5587d10cb6e0506")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

