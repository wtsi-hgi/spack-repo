# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95av2probe(RPackage):
	"""Probe sequence data for microarrays of type hgu95av2

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG_U95Av2_probe_tab.
	"""
	
	bioc = "hgu95av2probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95av2probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95av2probe/hgu95av2probe_2.18.0.tar.gz"]

	version("2.18.0", sha256="0f15ebc182b1bbd73f27e590d35414811f145374aec883ec80c92c429a566043")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

