# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu219probe(RPackage):
	"""Probe sequence data for microarrays of type hgu219

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U219_probe_tab.
	"""
	
	bioc = "hgu219probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu219probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu219probe/hgu219probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="a58eaaefcd9a73a485cc42b008e8ca3d00fab1fdf91ac6f742cfdfeb4bc2c56b")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

