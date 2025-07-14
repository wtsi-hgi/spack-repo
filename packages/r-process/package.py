# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcess(RPackage):
	"""Ciphergen SELDI-TOF Processing

	A package for processing protein mass spectrometry data.
	"""
	
	bioc = "PROcess"

	version("1.84.0", commit="73a3e7a666571afa565157ce0ff0bb124b7dd6fa")
	version("1.78.0", commit="62ebe36ba35611b99d32abf7f140f66003205f7e")

	depends_on("r-icens", type=("build", "run"))
