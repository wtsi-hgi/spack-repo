# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoli2probe(RPackage):
	"""Probe sequence data for microarrays of type ecoli2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was E_coli_2_probe_tab.
	"""
	
	bioc = "ecoli2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoli2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecoli2probe/ecoli2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="16554785116fbe3c0308f261ca7376a9ee1452a2ad27c22254574966819a0487")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

