# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene10stv1cdf(RPackage):
	"""mogene10stv1cdf

	A package containing an environment representing the MoGene-1_0-st-v1.cdf file.
	"""
	
	bioc = "mogene10stv1cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mogene10stv1cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mogene10stv1cdf/mogene10stv1cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="9c0271f5d6493290fc47f041a8c3f925")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation