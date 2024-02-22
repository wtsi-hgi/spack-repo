# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430aprobe(RPackage):
	"""Probe sequence data for microarrays of type htmg430a

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_MG-430A_probe_tab.
	"""
	
	bioc = "htmg430aprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/htmg430aprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/htmg430aprobe/htmg430aprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="e50cc49b8887b6ef8ee1152ec12d5010")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation