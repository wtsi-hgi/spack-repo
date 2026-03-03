# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPics(RPackage):
	"""Probabilistic inference of ChIP-seq

	Probabilistic inference of ChIP-Seq using an empirical Bayes mixture model approach.
	"""
	
	homepage = "https://github.com/SRenan/PICS"
	bioc = "PICS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PICS_2.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PICS/PICS_2.46.0.tar.gz"]

	version("2.46.0", md5="04ed3fdb7f1db15654e9974438495e43")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
