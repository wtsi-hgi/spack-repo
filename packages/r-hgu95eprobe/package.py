# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95eprobe(RPackage):
	"""Probe sequence data for microarrays of type hgu95e

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U95E_probe_tab.
	"""
	
	bioc = "hgu95eprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95eprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95eprobe/hgu95eprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="eb3fd8a745d9b425280aff59ddc918f5552cff32694d16d206aba7a4c9a74eb5")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

