# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetchem(RPackage):
	"""Chemical Structural Similarity Analysis

	A new pipeline to explore chemical structural similarity across metabolite. It allows to classify metabolites in structurally-related modules and identify common shared functional groups. KODAMA algorithm is used to highlight structural similarity between metabolites. See Cacciatore S, Tenori L, Luchinat C, Bennett PR, MacIntyre DA. (2017) Bioinformatics <doi:10.1093/bioinformatics/btw705>, Cacciatore S, Luchinat C, Tenori L. (2014) Proc Natl Acad Sci USA <doi:10.1073/pnas.1220873111>, and Abdel-Shafy EA, Melak T, MacIntyre DA, Zadra G, Zerbini LF, Piazza S, Cacciatore S. (2023) Bioinformatics Advances <doi:10.1093/bioadv/vbad053>.
	"""
	
	cran = "MetChem" 

	version("0.4", md5="6d15f7270bb6cde84c82387525cc77d5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kodama@2.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-fingerprint", type=("build", "run"))
	depends_on("r-rcdk@3.4.3:", type=("build", "run"))
