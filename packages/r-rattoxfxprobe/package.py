# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRattoxfxprobe(RPackage):
	"""Probe sequence data for microarrays of type rattoxfx

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RatToxFX_probe_tab.
	"""
	
	bioc = "rattoxfxprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rattoxfxprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rattoxfxprobe/rattoxfxprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="33a21ea8a61c5a3c405745a6c88350527ce907bc7e74037db26ce6514a2ae1ce")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

