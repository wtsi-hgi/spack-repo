# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacbehaviour(RPackage):
	"""Behavioural Studies of Large Language Models

	We provide an efficient way to design and conduct psycholinguistic experiments for testing the performance of large language models. It simplifies the process of setting up experiments, and data collection via large language models' API, streamlining workflow for researchers in the field of machine behavior. For methodology details, see Duan, X., Li, S., & Cai, Z. G. (2023) <doi:10.31234/osf.io/ywtfd>.
	"""
	
	cran = "MacBehaviour" 

	version("1.1.3", md5="5fb86e598075337abdeeab98c7c8e8e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
