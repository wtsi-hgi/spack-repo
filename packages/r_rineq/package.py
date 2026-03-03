# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRineq(RPackage):
	"""Concentration Index and Decomposition for Health Inequalities

	Relative, generalized, and Erreygers corrected concentration index; plot Lorenz curves; and decompose health
    inequalities into contributing factors. The package currently works with (generalized) linear models, survival models, complex survey models, and marginal effects probit models.
    originally forked by Brecht Devleesschauwer from the 'decomp' package  (no longer on CRAN), rineq is now maintained by Kaspar Walter Meili. Compared to the earlier 'rineq' version on 'github' by Brecht Devleesschauwer (<https://github.com/brechtdv/rineq>), the regression tree functionality has been removed.
    Improvements compared to earlier versions include improved plotting of decomposition and concentration, added functionality to calculate the concentration index with different methods, calculation of robust standard errors, and support for the decomposition analysis using marginal effects probit regression models. The development version is available at <https://github.com/kdevkdev/rineq>.
	"""
	
	homepage = "https://github.com/kdevkdev/rineq/"
	cran = "rineq" 

	version("0.2.3", md5="654a74b9abfbd766831fd3847fc4f7d0")

	depends_on("r@3.5:", type=("build", "run"))
