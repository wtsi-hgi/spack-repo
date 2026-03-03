# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScopro(RPackage):
	"""Score Projection Between in 'Vivo' and in 'Vitro' Datasets

	Assigns a score projection from 0 to 1 between a given in 'vivo' stage and each single cluster from an in 'vitro' dataset. The score is assigned based on the the fraction of specific markers of the in 'vivo' stage that are conserved in the in 'vitro' clusters <https://github.com/ScialdoneLab>.
	"""
	
	cran = "SCOPRO" 

	version("0.1.0", md5="41f7a144ef6dd481a866bdc9d9fc647c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
