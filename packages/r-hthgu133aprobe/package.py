# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133aprobe(RPackage):
	"""Probe sequence data for microarrays of type hthgu133a

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_HG-U133A_probe_tab.
	"""
	
	bioc = "hthgu133aprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133aprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133aprobe/hthgu133aprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="83cd0d1f7618296644c83f77a9131c4d5fb47f253bcbfff40f26c12054cf5639")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

