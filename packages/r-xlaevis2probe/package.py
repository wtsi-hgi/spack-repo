# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlaevis2probe(RPackage):
	"""Probe sequence data for microarrays of type xlaevis2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was X_laevis_2_probe_tab.
	"""
	
	bioc = "xlaevis2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/xlaevis2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/xlaevis2probe/xlaevis2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="62d52915ea00bdd3ef4940770b881dda526a63c4d2a892cf0601fa3ae25f306f")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

