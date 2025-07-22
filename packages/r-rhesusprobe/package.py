# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhesusprobe(RPackage):
	"""Probe sequence data for microarrays of type rhesus

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Rhesus_probe_tab.
	"""
	
	bioc = "rhesusprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rhesusprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rhesusprobe/rhesusprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="343afd4e0f5447a61cca2dd1e3e47669404abb646c59806620bdb2bbf9bea839")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

