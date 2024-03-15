# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexmix(RPackage):
	"""Flexible Mixture Modeling.

	A general framework for finite mixtures of regression models using the EM
	algorithm is implemented. The E-step and all data handling are provided,
	while the M-step can be supplied by the user to easily define new models.
	Existing drivers implement mixtures of standard linear models, generalized
	linear models and model-based clustering."""

	cran = "flexmix"

	license("GPL-2.0-or-later")

	version("2.3-19", md5="f527d75cdb77e567d6e3b29c386f7a34")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-modeltools@0.2.16:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
