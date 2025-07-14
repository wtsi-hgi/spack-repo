# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTbx20bamsubset(RPackage):
	"""Subset of BAM files from the "TBX20" experiment

	Dual transcriptional activator and repressor roles of TBX20 regulate adult cardiac structure and function. A subset of the RNA-Seq data.
	"""
	
	bioc = "TBX20BamSubset"

	version("1.44.0", commit="fed74e5b3282f87e00f035eb858e01666906ef37")
	version("1.38.0", commit="8616b9d70766d981a6f88196003fdd6f0ea065c0")

	depends_on("r-rsamtools@1.9.8:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))

