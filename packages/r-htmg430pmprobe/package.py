# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430pmprobe(RPackage):
	"""Probe sequence data for microarrays of type htmg430pm

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_MG-430_PM_probe_tab.
	"""
	
	bioc = "htmg430pmprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htmg430pmprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htmg430pmprobe/htmg430pmprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="25128aaf4faecb850eebe58a3306499a8372e2529c0a77547ecb0e6b9d088f09")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

