# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnu34probe(RPackage):
	"""Probe sequence data for microarrays of type rnu34

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RN-U34_probe_tab.
	"""
	
	bioc = "rnu34probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rnu34probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rnu34probe/rnu34probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="eb76e34a3348179821f0568a1f9749dcfc9d17e3ef0b8d79ec6e14b28382f2e7")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

