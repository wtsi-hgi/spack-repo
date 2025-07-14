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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GGPA_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GGPA/GGPA_1.14.0.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="b903872658e75e79aabe41cc7a3047c165762ad9e2d894fc88a1ee84f1eaab23")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
