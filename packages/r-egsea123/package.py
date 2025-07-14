# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgsea123(RPackage):
	"""Easy and efficient ensemble gene set testing with EGSEA

	R package that supports the workflow article `Easy and efficient ensemble gene set testing with EGSEA', Alhamdoosh et al. (2017), F1000Research, 6:2010.
	"""
	
	homepage = "https://f1000research.com/articles/6-2010"
	bioc = "EGSEA123"

	version("1.32.0", commit="0dd39f9414a8446405b4bf524c146ef5eb88cb8f")
	version("1.26.0", commit="fc25b6aa532bd4e0e65bda8978eea427e4bb2787")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-egsea@1.5.2:", type=("build", "run"))
	depends_on("r-limma@3.49.2:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))

