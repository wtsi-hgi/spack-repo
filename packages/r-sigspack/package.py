# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigspack(RPackage):
	"""Mutational Signature Estimation for Single Samples

	Single sample estimation of exposure to mutational signatures. Exposures to known mutational signatures are estimated for single samples, based on quadratic programming algorithms. Bootstrapping the input mutational catalogues provides estimations on the stability of these exposures. The effect of the sequence composition of mutational context can be taken into account by normalising the catalogues.
	"""
	
	homepage = "https://github.com/bihealth/SigsPack"
	bioc = "SigsPack" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SigsPack_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SigsPack/SigsPack_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="f5473843a7af8f8490c067c27c125822653b5b4994dc6c663ffd76c0027bb2e9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-bsgenome@1.46:", type=("build", "run"))
	depends_on("r-variantannotation@1.24.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
