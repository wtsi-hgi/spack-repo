# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlbook(RPackage):
	"""Datasets for the R/qtl Book

	Datasets for the book, A Guide to QTL Mapping with R/qtl.
    Broman and Sen (2009) <doi:10.1007/978-0-387-92125-9>.
	"""
	
	homepage = "http://rqtl.org/book"
	cran = "qtlbook" 

	version("0.18-8", md5="121d831e80884d147648dcd8a7aac6e4")

	depends_on("r@2.10.1:", type=("build", "run"))
