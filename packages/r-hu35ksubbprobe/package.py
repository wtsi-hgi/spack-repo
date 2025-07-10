# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubbprobe(RPackage):
	"""Probe sequence data for microarrays of type hu35ksubb

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Hu35KsubB_probe_tab.
	"""
	
	bioc = "hu35ksubbprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubbprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubbprobe/hu35ksubbprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="ecf80efb79cc0604cbc3adb69fd10d5453b146a36b7583bb9392fe68cf43b472")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

