# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtrat230pmprobe(RPackage):
	"""Probe sequence data for microarrays of type htrat230pm

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_Rat230_PM_probe_tab.
	"""
	
	bioc = "htrat230pmprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/htrat230pmprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/htrat230pmprobe/htrat230pmprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="e4deeca2dc406367ac4a347e370267cf")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation