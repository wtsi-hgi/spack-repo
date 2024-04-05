# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTest3probe(RPackage):
	"""Probe sequence data for microarrays of type test3

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Test3_probe_tab.
	"""
	
	bioc = "test3probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/test3probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/test3probe/test3probe_2.18.0.tar.gz"]

	version("2.18.0", md5="ffcbfee4e5c486fd03b2b9b64820340c")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

