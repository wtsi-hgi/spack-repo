# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoplarprobe(RPackage):
	"""Probe sequence data for microarrays of type poplar

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Poplar_probe_tab.
	"""
	
	bioc = "poplarprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/poplarprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/poplarprobe/poplarprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="62bf69b1c908080155f5cd4fef35b1f8876a01aafd3a0f344e24d33127a426de")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

