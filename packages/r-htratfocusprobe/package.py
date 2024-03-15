# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtratfocusprobe(RPackage):
	"""Probe sequence data for microarrays of type htratfocus

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_Rat-Focus_probe_tab.
	"""
	
	bioc = "htratfocusprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htratfocusprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htratfocusprobe/htratfocusprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="26a0963d8aff314a4a1f2c47e9147a8a")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation