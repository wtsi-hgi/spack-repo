# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpa(RPackage):
	"""graph-GPA: A graphical model for prioritizing GWAS results and investigating pleiotropic architecture

	Genome-wide association studies (GWAS) is a widely used tool for identification of genetic variants associated with phenotypes and diseases, though complex diseases featuring many genetic variants with small effects present difficulties for traditional these studies. By leveraging pleiotropy, the statistical power of a single GWAS can be increased. This package provides functions for fitting graph-GPA, a statistical framework to prioritize GWAS results by integrating pleiotropy. 'GGPA' package provides user-friendly interface to fit graph-GPA models, implement association mapping, and generate a phenotype graph.
	"""
	
	homepage = "https://github.com/dongjunchung/GGPA/"
	bioc = "GGPA"

	version("1.20.0", commit="1a5d999ff9495d07240954bd3f5602d4e4fa45d7")
	version("1.14.0", commit="c28c9830663d30fad285fafde827d73dffb1515e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
