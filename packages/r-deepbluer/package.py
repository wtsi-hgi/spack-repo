# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepbluer(RPackage):
	"""DeepBlueR

	Accessing the DeepBlue Epigenetics Data Server through R.
	"""
	
	bioc = "DeepBlueR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DeepBlueR_1.27.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DeepBlueR/DeepBlueR_1.27.0.tar.gz"]

	version("1.27.0", md5="2217f4325cc72c3e22c330fa3a8dd25b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-diffr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-filehash", type=("build", "run"))
