# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74bprobe(RPackage):
	"""Probe sequence data for microarrays of type mgu74b

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MG-U74B_probe_tab.
	"""
	
	bioc = "mgu74bprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74bprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74bprobe/mgu74bprobe_2.18.0.tar.gz"]

	version("2.18.0", md5="224d606e6fc87592d387dbaabe5cd353")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

	# annotation