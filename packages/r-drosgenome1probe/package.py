# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosgenome1probe(RPackage):
	"""Probe sequence data for microarrays of type drosgenome1

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was DrosGenome1_probe_tab.
	"""
	
	bioc = "drosgenome1probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/drosgenome1probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/drosgenome1probe/drosgenome1probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="28c506791b89140cdb548bf1d378352d18cf26ed4e5da76ec36d4d7b5240eeef")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

