# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbkrtest(RPackage):
	"""Parametric Bootstrap, Kenward-Roger and Satterthwaite Based Methods for
	Test in Mixed Models.

	Test in mixed effects models. Attention is on mixed effects models as
	implemented in the 'lme4' package. For linear mixed models, this package
	implements (1) a parametric bootstrap test, (2) a Kenward-Roger-typ
	modification of F-tests for linear mixed effects models and (3) a
	Satterthwaite-type modification of F-tests for linear mixed effects models.
	The package also implements a parametric bootstrap test for generalized
	linear mixed models.  The facilities of the package are documented in the
	paper by Halehoh and Hojsgaard, (2012, <doi:10.18637/jss.v059.i09>).
	Please see 'citation("pbkrtest")' for citation details."""

	cran = "pbkrtest"

	version("0.5.2", md5="bee5ef60cb7cb13ceab1902284c63074")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lme4@1.1.31:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix@1.2.3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
