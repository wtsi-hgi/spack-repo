# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrio(RPackage):
	"""Testing of SNPs and SNP Interactions in Case-Parent Trio Studies

	Testing SNPs and SNP interactions with a genotypic TDT. This package furthermore contains functions for computing pairwise values of LD measures and for identifying LD blocks, as well as functions for setting up matched case pseudo-control genotype data for case-parent trios in order to run trio logic regression, for imputing missing genotypes in trios, for simulating case-parent trios with disease risk dependent on SNP interaction, and for power and sample size calculation in trio data.
	"""
	
	bioc = "trio" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/trio_3.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/trio/trio_3.40.0.tar.gz"]

    version("3.46.0", tag="RELEASE_3_21")
	version("3.40.0", sha256="1bb69d82f53432e83f108eaaee530bcc6a73191d0e31fed22eb13d2dcf740342")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-siggenes", type=("build", "run"))
	depends_on("r-logicreg@1.6.1:", type=("build", "run"))
