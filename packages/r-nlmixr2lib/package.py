# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmixr2lib(RPackage):
	"""A Model Library for 'nlmixr2'

	A model library for 'nlmixr2'.  The models include
  (and plan to include) pharmacokinetic, pharmacodynamic, and
  disease models used in pharmacometrics.  Where applicable,
  references for each model are included in the meta-data for
  each individual model.  The package also includes model
  composition and modification functions to make model updates
  easier.
	"""
	
	homepage = "https://github.com/nlmixr2/nlmixr2lib"
	cran = "nlmixr2lib" 

	version("0.2.0", md5="562d1e87b889e334f286b3b642e49c7b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-nlmixr2est", type=("build", "run"))
	depends_on("r-rxode2@2.0.12:", type=("build", "run"))
