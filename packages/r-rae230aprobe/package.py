# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230aprobe(RPackage):
	"""Probe sequence data for microarrays of type rae230a

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RAE230A_probe_tab.
	"""
	
	bioc = "rae230aprobe" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rae230aprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rae230aprobe/rae230aprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="6f2d77e1d9c1e3afb96ef78b3202bb0b")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation