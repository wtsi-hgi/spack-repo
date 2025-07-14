# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrlmm(RPackage):
	"""Genotype Calling (CRLMM) and Copy Number Analysis tool for Affymetrix SNP 5.0 and 6.0 and Illumina arrays

	Faster implementation of CRLMM specific to SNP 5.0 and 6.0 arrays, as well as a copy number tool specific to 5.0, 6.0, and Illumina platforms.
	"""
	
	bioc = "crlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/crlmm_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/crlmm/crlmm_1.60.0.tar.gz"]

    version("1.66.0", tag="RELEASE_3_21")
	version("1.60.0", sha256="722e1d169bc6c8b2f2e9a685c76bcb2ebe8ce6e3d89a80b2b302809e3ed987df")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-oligoclasses@1.21.12:", type=("build", "run"))
	depends_on("r-preprocesscore@1.17.7:", type=("build", "run"))
	depends_on("r-biobase@2.15.4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-affyio@1.23.2:", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.1.2.1:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-beanplot", type=("build", "run"))
