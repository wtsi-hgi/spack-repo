# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoybeanprobe(RPackage):
	"""Probe sequence data for microarrays of type soybean

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Soybean_probe_tab.
	"""
	
	bioc = "soybeanprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/soybeanprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/soybeanprobe/soybeanprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="3057a5c387ff35b6c647c4db27041a13")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

