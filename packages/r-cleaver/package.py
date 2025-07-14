# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleaver(RPackage):
	"""Cleavage of Polypeptide Sequences

	In-silico cleavage of polypeptide sequences. The cleavage rules are taken from: http://web.expasy.org/peptide_cutter/peptidecutter_enzymes.html
	"""
	
	homepage = "https://github.com/sgibb/cleaver/"
	bioc = "cleaver" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cleaver_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cleaver/cleaver_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="53417e207e8bb617d31f8385cc68849e8a3c2494e3c31790ac2edbce6c062a64")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biostrings@1.29.8:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
