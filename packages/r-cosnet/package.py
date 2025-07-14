# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosnet(RPackage):
	"""Cost Sensitive Network for node label prediction on graphs with highly unbalanced labelings

	Package that implements the COSNet classification algorithm. The algorithm predicts node labels in partially labeled graphs where few positives are available for the class being predicted.
	"""
	
	homepage = "https://github.com/m1frasca/COSNet_GitHub"
	bioc = "COSNet"

	version("1.42.0", commit="d3fa1c7d19c26aaec646537a5da542cf465bbf4f")
	version("1.36.0", commit="6c45ee840ee5303329d96a76320ea011c37d3d8c")

