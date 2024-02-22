# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsaur(RPackage):
	"""Data Sets for "Applied Survival Analysis Using R""

	Data sets are referred to in the text "Applied Survival Analysis Using R"
 by Dirk F. Moore, Springer, 2016, ISBN: 978-3-319-31243-9, <DOI:10.1007/978-3-319-31245-3>.
	"""
	
	cran = "asaur" 

	version("0.50", md5="42960895df4da99f084abc9ab6256269")

