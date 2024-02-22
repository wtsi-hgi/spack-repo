# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAmelliferaBeebaseAssembly4(RPackage):
	"""Full genome sequences for Apis mellifera (BeeBase assembly4)

	iFull genome sequences for Apis mellifera (Honey Bee) as provided by BeeBase (assembly4, Feb. 2008) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Amellifera.BeeBase.assembly4" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Amellifera.BeeBase.assembly4_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Amellifera.BeeBase.assembly4/BSgenome.Amellifera.BeeBase.assembly4_1.4.0.tar.gz"]

	version("1.4.0", md5="77495ee5eba48fe52902c9cc4f9ba7cc", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Amellifera.BeeBase.assembly4_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation