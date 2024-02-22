# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPharmaverse(RPackage):
	"""Navigate 'Pharmaverse'

	The 'pharmaverse' is a set of packages that compose multiple pathways 
    through clinical data generation and reporting in the pharmaceutical industry.
    This package is designed to guide users to our work-spaces on 'GitHub', 'Slack' 
    and 'LinkedIn' as well as our website and examples.
    Learn more about the 'pharmaverse' at <https://pharmaverse.org>.
	"""
	
	homepage = "https://github.com/pharmaverse/pharmaverse-pkg"
	cran = "pharmaverse" 

	version("0.0.2", md5="982ccb0633e759741f70324b44e297d8")

	depends_on("r-httr", type=("build", "run"))
