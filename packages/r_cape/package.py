# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCape(RPackage):
	"""Combined Analysis of Pleiotropy and Epistasis for Diversity
Outbred Mice

	Combined Analysis of Pleiotropy and Epistasis infers predictive 
    networks between genetic variants and phenotypes. It can be used with 
    standard two-parent populations as well as multi-parent populations, such 
    as the Diversity Outbred (DO) mice, Collaborative Cross (CC) mice, or the 
    multi-parent advanced generation intercross (MAGIC) population of Arabidopsis
    thaliana. It uses complementary information of pleiotropic gene variants across
    different phenotypes to resolve models of epistatic interactions between alleles. 
    To do this, cape reparametrizes main effect and interaction coefficients from
    pairwise variant regressions into directed influence parameters. These
    parameters describe how alleles influence each other, in terms of suppression 
    and enhancement, as well as how gene variants influence phenotypes. All of the 
    final interactions are reported as directed interactions between pairs of 
    parental alleles. For detailed descriptions of the methods used in this package 
    please see the following references.
    Carter, G. W., Hays, M., Sherman, A. & Galitski, T. (2012) <doi:10.1371/journal.pgen.1003010>.
    Tyler, A. L., Lu, W., Hendrick, J. J., Philip, V. M. & Carter, G. W. (2013) <doi:10.1371/journal.pcbi.1003270>.
	"""
	
	cran = "cape" 

	version("3.1.2", md5="8f299d8bf4ac38101031655bc8248b0a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-propagate", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-qtl2", type=("build", "run"))
	depends_on("r-qtl2convert", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-regress@1.3.21:", type=("build", "run"))
	depends_on("r-shape@1.4.5:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
