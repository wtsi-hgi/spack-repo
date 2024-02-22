# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgenetics(RPackage):
	"""R packages for genetics research

	R packages for genetics research
	"""
	
	cran = "RGenetics" 

	version("0.1", md5="7bf0c2f9b476ba6a8628e618a9a46381")

