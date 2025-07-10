# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiceprobe(RPackage):
	"""Probe sequence data for microarrays of type rice

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Rice_probe_tab.
	"""
	
	bioc = "riceprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/riceprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/riceprobe/riceprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="2a8792f4cb9975d38207ad2f09a28549095f4f37a4d125f6b037dadabeded870")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

