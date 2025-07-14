# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgacrcmirna(RPackage):
	"""TCGA CRC 450 miRNA dataset

	colorectal cancer miRNA profile provided by TCGA
	"""
	
	bioc = "TCGAcrcmiRNA"

	version("1.28.0", commit="6b2fec99d5870600741443c6808b7e5fb779b833")
	version("1.22.0", commit="4ba030de8ac10055e337ff3c604e40464d051f58")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

