# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34aprobe(RPackage):
	"""Probe sequence data for microarrays of type rgu34a

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RG-U34A_probe_tab.
	"""
	
	bioc = "rgu34aprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34aprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34aprobe/rgu34aprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="90364414a8c439e00152b289e8cfe7c33da93241cea0c1e2d84f221112f65dbe")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

