# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaureuscdf(RPackage):
	"""saureuscdf

	A package containing an environment representing the S_aureus.cdf file.
	"""
	
	bioc = "saureuscdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/saureuscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/saureuscdf/saureuscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="d01883e4c3dd99f32012e6dbab8cdb8b")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation