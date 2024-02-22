# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmelting(RPackage):
	"""R Interface to MELTING 5

	R interface to the MELTING 5 program (https://www.ebi.ac.uk/biomodels/tools/melting/) to compute melting temperatures of nucleic acid duplexes along with other thermodynamic parameters.
	"""
	
	homepage = "https://github.com/aravind-j/rmelting"
	bioc = "rmelting" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rmelting_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rmelting/rmelting_1.18.0.tar.gz"]

	version("1.18.0", md5="a73d7dd41b3d77dce067644b04412e9d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))
