# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenford(RPackage):
	"""Benford's Analysis on Large Data Sets

	Perform the Benford's Analysis to a data set in order to evaluate if it contains human fabricated data. For more details on the method see Moreau, 2021, Model Assist. Statist. Appl., 16 (2021) 73–79. <doi:10.3233/MAS-210517>.
	"""
	
	cran = "benford" 

	version("1.0.1", md5="d1251ab8f4076ec8b06f04cb7436a0b4")

	depends_on("r@3.5:", type=("build", "run"))
