# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZalpha(RPackage):
	"""Run a Suite of Selection Statistics

	A suite of statistics for identifying areas of the genome under selective pressure. See Jacobs, Sluckin and Kivisild (2016) <doi:10.1534/genetics.115.185900>.
	"""
	
	cran = "zalpha" 

	version("0.3.0", md5="babece313b7206135ed9e62330e9893e")

	depends_on("r@2.10:", type=("build", "run"))
