# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedadipochip(RPackage):
	"""A Curated ChIP-Seq Dataset of MDI-induced Differentiated Adipocytes (3T3-L1)

	A curated dataset of publicly available ChIP-sequencing of transcription factors, chromatin remodelers and histone modifications in the 3T3-L1 pre-adipocyte cell line. The package document the data collection, pre-processing and processing of the data. In addition to the documentation, the package contains the scripts that was used to generated the data.
	"""
	
	homepage = "https://github.com/MahShaaban/curatedAdipoChIP"
	bioc = "curatedAdipoChIP"

	version("1.24.0", commit="3538b4c71ce0ba2aa509dbe2f5da98e946bfd547")
	version("1.18.0", commit="c130c9b6354bee43b12e2e296d5b2a7f86a504df")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

