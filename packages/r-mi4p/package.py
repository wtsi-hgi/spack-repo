# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMi4p(RPackage):
	"""Multiple Imputation for Proteomics

	A framework for multiple imputation for proteomics is proposed by Marie Chion, Christine Carapito and Frederic Bertrand (2021) <arxiv:2108.07086>. It is dedicated to dealing with multiple imputation for proteomics.
	"""
	
	homepage = "https://mariechion.github.io/mi4p/"
	cran = "mi4p" 

	version("1.1", md5="bdc8d75a1a2ba8722893e4222d302310")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-imp4p", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
