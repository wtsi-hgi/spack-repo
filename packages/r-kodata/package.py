# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKodata(RPackage):
	"""LINCS Knock-Out Data Package

	Contains consensus genomic signatures (CGS) for experimental cell-line specific gene knock-outs as well as baseline gene expression data for a subset of experimental cell-lines. Intended for use with package KEGGlincs.
	"""
	
	bioc = "KOdata"

	version("1.34.0", commit="3119d163ef78f3b8704841017e18063705978f4e")
	version("1.28.0", commit="414127279bfdd53838dd0a8eb22840ef94f095b1")

	depends_on("r@3.3:", type=("build", "run"))

