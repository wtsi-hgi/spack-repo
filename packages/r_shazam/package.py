# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShazam(RPackage):
	"""Immunoglobulin Somatic Hypermutation Analysis

	Provides a computational framework for analyzing mutations in
    immunoglobulin (Ig) sequences. Includes methods for Bayesian estimation of
    antigen-driven selection pressure, mutational load quantification, building of
    somatic hypermutation (SHM) models, and model-dependent distance calculations.
    Also includes empirically derived models of SHM for both mice and humans.
    Citations: 
    Gupta and Vander Heiden, et al (2015) <doi:10.1093/bioinformatics/btv359>, 
    Yaari, et al (2012) <doi:10.1093/nar/gks457>, 
    Yaari, et al (2013) <doi:10.3389/fimmu.2013.00358>, 
    Cui, et al (2016) <doi:10.4049/jimmunol.1502263>.
	"""
	
	homepage = "http://shazam.readthedocs.io"
	cran = "shazam" 

	version("1.2.0", md5="47966d84c090fe8f6cc3f0d0cdf778c6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-alakazam@1.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph@1.5:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringi@1.1.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
