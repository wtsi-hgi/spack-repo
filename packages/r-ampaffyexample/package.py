# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmpaffyexample(RPackage):
	"""Example of Amplified Data

	Six arrays. Three from amplified RNA, three from the typical procedure.
	"""
	
	homepage = "https://bioconductor.org/packages/AmpAffyExample"
	bioc = "AmpAffyExample"

	version("1.48.0", commit="f8a3c2ddd3831dcf0b8bd2e8e5fcd82d0948d46e")
	version("1.42.0", commit="62d3a82843d25c52379b81bc92d79a5b7cbaf079")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

