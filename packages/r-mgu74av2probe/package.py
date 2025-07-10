# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74av2probe(RPackage):
	"""Probe sequence data for microarrays of type mgu74av2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MG-U74Av2_probe_tab.
	"""
	
	bioc = "mgu74av2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74av2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74av2probe/mgu74av2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="5fe43d2b50f1ef405c2e0482569160c57d3a45e0aef395bd83a375557d0f8e0b")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

