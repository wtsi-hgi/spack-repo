# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTomatoprobe(RPackage):
	"""Probe sequence data for microarrays of type tomato

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Tomato_probe_tab.
	"""
	
	bioc = "tomatoprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/tomatoprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/tomatoprobe/tomatoprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="22b9ebb6cdbb685bd45c4c6e576db85f1d99b114d76220efb96925456ffd48aa")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

