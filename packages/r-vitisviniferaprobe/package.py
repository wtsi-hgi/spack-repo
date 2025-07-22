# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVitisviniferaprobe(RPackage):
	"""Probe sequence data for microarrays of type vitisvinifera

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Vitis_Vinifera_probe_tab.
	"""
	
	bioc = "vitisviniferaprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/vitisviniferaprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/vitisviniferaprobe/vitisviniferaprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="2a8de8bcd2d2914fc2a46378a8357eeb5c05fd8e4cf44d249c79f376860effbd")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

