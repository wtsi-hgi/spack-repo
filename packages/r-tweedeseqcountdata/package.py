# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTweedeseqcountdata(RPackage):
	"""RNA-seq count data employed in the vignette of the tweeDEseq package

	RNA-seq count data from Pickrell et al. (2010) employed to illustrate the use of the Poisson-Tweedie family of distributions with the tweeDEseq package.
	"""
	
	homepage = "https://github.com/isglobal-brge/tweeDEseqCountData/"
	bioc = "tweeDEseqCountData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/tweeDEseqCountData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/tweeDEseqCountData/tweeDEseqCountData_1.40.0.tar.gz"]

	version("1.40.0", sha256="db14f527829f488876baed853758cb299462bf4a6d66ea8929b8518c4e0907e8")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@4.3:", type=("build", "run"))

