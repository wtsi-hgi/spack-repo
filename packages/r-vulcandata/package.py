# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVulcandata(RPackage):
	"""VirtUaL ChIP-Seq data Analysis using Networks, dummy dataset

	This package provides a dummy regulatory network and ChIP-Seq dataset for running examples in the vulcan package
	"""
	
	bioc = "vulcandata"

	version("1.30.0", commit="be1b0adba1f8b47b9f6b0f58ba2bc4914fe89577")
	version("1.24.0", commit="efadc13d448153e8198b7fece08eb028ec11b95d")


