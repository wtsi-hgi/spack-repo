# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReprestools(RPackage):
	"""Reproducible Research Tools

	Reproducible research tools automates the creation of an analysis directory structure and work flow. There are R markdown
  skeletons which encapsulate typical analytic work flow steps. Functions will create appropriate modules which may
  pass data from one step to another.
	"""
	
	homepage = "https://pirategrunt.com/represtools/"
	cran = "represtools" 

	version("0.1.3", md5="5c1054de7328f094ce0e22070c859e7e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
