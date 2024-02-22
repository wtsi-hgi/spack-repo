# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanvasxpressData(RPackage):
	"""Datasets for the 'canvasXpress' Package

	Contains the prepared data that is needed for the 'shiny' application examples in the 
    'canvasXpress' package.  This package also includes datasets used for automated 'testthat' tests.
    Scotto L, Narayan G, Nandula SV, Arias-Pulido H et al. (2008) <doi:10.1002/gcc.20577>.
    Davis S, Meltzer PS (2007) <doi:10.1093/bioinformatics/btm254>.
	"""
	
	homepage = "https://github.com/neuhausi/canvasXpress.data"
	cran = "canvasXpress.data" 

	version("1.34.2", md5="0df166053851e54ba49dca573d21080a")

	depends_on("r@3.5:", type=("build", "run"))
