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

	version("2.52.0", tag="RELEASE_3_21")
	version("2.46.0", sha256="cbfe9cc744144aa0087d360eba98c4adb103307e162193c32d1f265a348aed66")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
