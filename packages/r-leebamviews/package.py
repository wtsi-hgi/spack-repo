# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeebamviews(RPackage):
	"""leeBamViews -- multiple yeast RNAseq samples excerpted from Lee 2009

	data from PMID 19096707; prototype for managing multiple NGS samples
	"""
	
	bioc = "leeBamViews"

	version("1.44.0", commit="1a0f16fc9d7aa0fb1948c77942e941a1f841f332")
	version("1.38.0", commit="98ea87d892a5e586bcf19e24ac105e4f8f962cf0")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rsamtools@0.1.50:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))

