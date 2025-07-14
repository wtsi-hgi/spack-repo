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

	version("1.22.0", commit="55a66b0ee860f3887a1ab4ca5a3c4ffc5c6a52c7")
	version("1.16.0", commit="bbf57096ede9a2766a84c63294a0df9a03f048ba")

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
