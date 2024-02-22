# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCepiigeodist(RPackage):
	"""CEPII's GeoDist Datasets

	Provides data on countries and their main city or agglomeration and
    the different distance measures and dummy variables indicating whether two
    countries are contiguous, share a common language or a colonial
    relationship. The reference article for these datasets is Mayer and Zignago
    (2011) <http://www.cepii.fr/CEPII/en/publications/wp/abstract.asp?NoDoc=3877>.
	"""
	
	homepage = "https://pacha.dev/cepiigeodist/"
	cran = "cepiigeodist" 

	version("0.1", md5="eaecaef7c4a3e95977bb3abed0d663ec")

	depends_on("r@2.10:", type=("build", "run"))
