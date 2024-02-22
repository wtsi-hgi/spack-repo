# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDagwood(RPackage):
	"""DAGs with Omitted Objects Displayed (DAGWOOD)

	DAGs With Omitted Objects Displayed (DAGWOOD) is a framework to help reveal key hidden assumptions in a causal DAG. This package provides an implementation of the DAGWOOD algorithm. Further description can be found in Haber et al (2022) <DOI:10.1016/j.annepidem.2022.01.001>.
	"""
	
	cran = "dagwood" 

	version("0.1.4", md5="e4552ae1a565bd02dae441375f1b661d")

	depends_on("r-dagitty", type=("build", "run"))
