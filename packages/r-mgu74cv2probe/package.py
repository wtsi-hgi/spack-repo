# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74cv2probe(RPackage):
	"""Probe sequence data for microarrays of type mgu74cv2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MG-U74Cv2_probe_tab.
	"""
	
	bioc = "mgu74cv2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74cv2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74cv2probe/mgu74cv2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="c6e1efa36de917bc933cf374b02dd26ccc310d746b01ba11a97691a85f64a267")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

