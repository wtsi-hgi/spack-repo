# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133acdf(RPackage):
	"""hthgu133acdf

	A package containing an environment representing the HT_HG-U133A.cdf file.
	"""
	
	bioc = "hthgu133acdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133acdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133acdf/hthgu133acdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="37e34f31748cf269614f48095c584262db2bb98b5df69cebf0dd824e8320aba8")

	depends_on("r-annotationdbi", type=("build", "run"))

