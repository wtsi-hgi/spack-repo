# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModcon(RPackage):
	"""Modifying splice site usage by changing the mRNP code, while maintaining the genetic code

	Collection of functions to calculate a nucleotide sequence surrounding for splice donors sites to either activate or repress donor usage. The proposed alternative nucleotide sequence encodes the same amino acid and could be applied e.g. in reporter systems to silence or activate cryptic splice donor sites.
	"""
	
	homepage = "https://github.com/caggtaagtat/ModCon"
	bioc = "ModCon" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ModCon_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ModCon/ModCon_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="5c22734c752cc7998326b4be8eb5041e782d9c15fdc51c2168f4ce0d6f413f9d")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
