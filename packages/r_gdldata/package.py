# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdldata(RPackage):
	"""'Global Data Lab' R API

	Retrieve datasets from the 'Global Data Lab' website <https://globaldatalab.org>
    directly into R data frames. Functions are provided to reference available options
    (indicators, levels, countries, regions) as well.
	"""
	
	homepage = "https://docs.globaldatalab.org/gdldata/"
	cran = "gdldata" 

	version("0.1", md5="ee81e49f60e6e8770a0fdcd11550c274")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
