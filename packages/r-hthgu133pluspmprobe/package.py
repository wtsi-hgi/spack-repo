# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133pluspmprobe(RPackage):
	"""Probe sequence data for microarrays of type hthgu133pluspm

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_HG-U133_Plus_PM_probe_tab.
	"""
	
	bioc = "hthgu133pluspmprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133pluspmprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133pluspmprobe/hthgu133pluspmprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="e7628ed138d14932e3925051b91062446ec3ffd420138b907424b3b20ccfcf45")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

