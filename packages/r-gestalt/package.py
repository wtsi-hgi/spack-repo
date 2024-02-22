# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGestalt(RPackage):
	"""Tools for Making and Combining Functions

	Provides a suite of function-building tools centered around a
  (forward) composition operator, %>>>%, which extends the semantics of the
  'magrittr' %>% operator and supports 'Tidyverse' quasiquotation. It enables
  you to construct composite functions that can be inspected and transformed as
  list-like objects. In conjunction with %>>>%, a compact function constructor,
  fn(), and a partial-application constructor, partial(), are also provided;
  both support quasiquotation.
	"""
	
	homepage = "https://github.com/egnha/gestalt"
	cran = "gestalt" 

	version("0.2.0", md5="e3d9b1abc7c4eb4bdf9e386d837c14c1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
