# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlpca(RPackage):
	"""The Distributed Local PCA Algorithm

	Algorithm to handle with optimal subset selection for distributed local principal component analysis. The philosophy of the package is described in Guo G. (2020) <doi:10.1080/02331888.2020.1823979>.
	"""
	
	cran = "DLPCA" 

	version("0.0.5", md5="8834dc11aa539b8c099e494a1bf93054")

	depends_on("r@3.5:", type=("build", "run"))
