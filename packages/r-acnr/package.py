# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcnr(RPackage):
	"""Annotated Copy-Number Regions

	Provides SNP array data from different types of
    copy-number regions. These regions were identified manually by the authors
    of the package and may be used to generate realistic data sets with known
    truth.
	"""
	
	homepage = "https://github.com/mpierrejean/acnr"
	cran = "acnr" 

	version("1.0.0", md5="df1eefcc652c0676beaebbdc240f244f")

	depends_on("r@2.10:", type=("build", "run"))
