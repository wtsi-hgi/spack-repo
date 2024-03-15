# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaretensemble(RPackage):
	"""Ensembles of Caret Models.

	Functions for creating ensembles of caret models: caretList() and
	caretStack(). caretList() is a convenience function for fitting multiple
	caret::train() models to the same dataset. caretStack() will make linear or
	non-linear combinations of these models, using a caret::train() model as a
	meta-model, and caretEnsemble() will make a robust linear combination of
	models using a GLM."""

	cran = "caretEnsemble"

	license("MIT")

	version("2.0.3", md5="85932479e273cf59b579a037442b7619")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
