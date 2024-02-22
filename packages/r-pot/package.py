# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPot(RPackage):
	"""Generalized Pareto Distribution and Peaks Over Threshold

	Some functions useful to perform a Peak Over Threshold
        analysis in univariate and bivariate cases, see Beirlant et al. (2004)
        <doi:10.1002/0470012382>. A user guide is available in the vignette.
	"""
	
	homepage = "https://pot.r-forge.r-project.org/"
	cran = "POT" 

	version("1.1-10", md5="305a233ce4f5d993e9fab2afcc1a29f3")

	depends_on("r@3:", type=("build", "run"))
