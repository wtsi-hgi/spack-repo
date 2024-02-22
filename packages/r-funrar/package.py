# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunrar(RPackage):
	"""Functional Rarity Indices Computation

	Computes functional rarity indices as proposed by Violle et al.
    (2017) <doi:10.1016/j.tree.2017.02.002>. Various indices can be computed
    using both regional and local information. Functional Rarity combines both
    the functional aspect of rarity as well as the extent aspect of rarity.
    'funrar' is presented in Grenié et al. (2017) <doi:10.1111/ddi.12629>.
	"""
	
	homepage = "https://rekyt.github.io/funrar/"
	cran = "funrar" 

	version("1.5.0", md5="954e0021a172a877eb8032f430693db3")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
