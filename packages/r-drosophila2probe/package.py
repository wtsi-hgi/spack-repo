# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosophila2probe(RPackage):
	"""Probe sequence data for microarrays of type drosophila2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Drosophila_2_probe_tab.
	"""
	
	bioc = "drosophila2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/drosophila2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/drosophila2probe/drosophila2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="11d04b7d032e0d318c1472dd27ba0eda6b5992f0eba839b473ec5cf0fcb41cad")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

