# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaeg1aprobe(RPackage):
	"""Probe sequence data for microarrays of type paeg1a

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was P_aeg1a_probe_tab.
	"""
	
	bioc = "paeg1aprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/paeg1aprobe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/paeg1aprobe/paeg1aprobe_2.18.0.tar.gz"]

	version("2.18.0", sha256="de2fe281ee7882e93ced9482e91edc3245fd85b3d08ef484ff36392e00697e41")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

