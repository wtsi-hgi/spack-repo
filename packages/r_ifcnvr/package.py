# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfcnvr(RPackage):
	"""Isolation-Forest Based 'CNV' Detection from 'NGS' Data

	Automatically detects Copy Number Variations (CNV) from Next Generation Sequencing data using a machine learning algorithm, Isolation forest. More details about the method can be found in the paper by Cabello-Aguilar (2022) <doi:10.1101/2022.01.03.474771>.
	"""
	
	homepage = "https://github.com/SimCab-CHU/ifCNVR"
	cran = "ifCNVR" 

	version("0.1.0", md5="78f120e3fdc2a062c6ddfaf9f1f62a97")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-isotree", type=("build", "run"))
