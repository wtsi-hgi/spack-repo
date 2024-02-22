# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDragonking(RPackage):
	"""Statistical Tools to Identify Dragon Kings

	Statistical tests and test statistics to identify events in a
    dataset that are dragon kings (DKs). The statistical methods in this
    package were reviewed in Wheatley & Sornette (2015) <doi:10.2139/ssrn.2645709>.
	"""
	
	homepage = "https://github.com/rrrlw/dragonking"
	cran = "dragonking" 

	version("0.1.0", md5="5ad72a4b2993d663434acf84caaddf5c")

