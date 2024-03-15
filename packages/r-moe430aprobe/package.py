# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoe430aprobe(RPackage):
	"""Probe sequence data for microarrays of type moe430a

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MOE430A_probe_tab.
	"""
	
	bioc = "moe430aprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/moe430aprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/moe430aprobe/moe430aprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="0aa83189d04599a65211d1a2f0a51c8f")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation