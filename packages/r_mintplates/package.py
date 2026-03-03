# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMintplates(RPackage):
	"""Encode "License-Plates" from Sequences and Decode Them Back

	It can be used to create/encode molecular "license-plates" from sequences and to also decode the "license-plates" back to sequences.  While initially created for transfer RNA-derived small fragments (tRFs), this tool can be used for any genomic sequences including but not limited to: tRFs, microRNAs, etc. The detailed information can reference to Pliatsika V, Loher P, Telonis AG, Rigoutsos I (2016) <doi:10.1093/bioinformatics/btw194>. It can also be used to annotate tRFs. The detailed information can reference to Loher P, Telonis AG, Rigoutsos I (2017) <doi:10.1038/srep41184>.
	"""
	
	homepage = "http://www.bio-inf.cn/"
	cran = "MINTplates" 

	version("1.0.1", md5="4b3b7c3f9c579187ac2dd8aa014501e6")

	depends_on("r@3.2.3:", type=("build", "run"))
