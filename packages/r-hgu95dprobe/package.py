# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95dprobe(RPackage):
	"""Probe sequence data for microarrays of type hgu95d

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U95D_probe_tab.
	"""
	
	bioc = "hgu95dprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95dprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95dprobe/hgu95dprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="cfc4deb5507f89240e3e51f3467474c371b1ebfd5748984100412c8118129256")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

