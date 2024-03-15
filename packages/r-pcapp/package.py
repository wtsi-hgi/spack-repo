# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcapp(RPackage):
	"""Provides functions for robust PCA by projection pursuit.

	Provides functions for robust PCA by projection pursuit. The methods are
	described in Croux et al. (2006) <doi:10.2139/ssrn.968376>, Croux et al.
	(2013) <doi:10.1080/00401706.2012.727746>, Todorov and Filzmoser (2013)
	<doi:10.1007/978-3-642-33042-1_31>."""

	cran = "pcaPP"

	version("2.0-4", md5="1d4f3e97f1fca7cd3f476f33740b87c9")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
