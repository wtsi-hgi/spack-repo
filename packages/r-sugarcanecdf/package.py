# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSugarcanecdf(RPackage):
	"""sugarcanecdf

	A package containing an environment representing the Sugar_Cane.cdf file.
	"""
	
	bioc = "sugarcanecdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/sugarcanecdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/sugarcanecdf/sugarcanecdf_2.18.0.tar.gz"]

	version("2.18.0", md5="f66d51868068f83d3693d3cb05be418a")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation