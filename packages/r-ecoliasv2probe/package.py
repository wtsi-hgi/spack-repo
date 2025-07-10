# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoliasv2probe(RPackage):
	"""Probe sequence data for microarrays of type ecoliasv2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was E_coli_Asv2_probe_tab.
	"""
	
	bioc = "ecoliasv2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoliasv2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecoliasv2probe/ecoliasv2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="63da83fa86a814a85ed2dc7472cfc1514b59ceb2de5627d88b8d8113a8b2d9c1")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

