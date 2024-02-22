# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedicagocdf(RPackage):
	"""medicagocdf

	A package containing an environment representing the Medicago.cdf file.
	"""
	
	bioc = "medicagocdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/medicagocdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/medicagocdf/medicagocdf_2.18.0.tar.gz"]

	version("2.18.0", md5="1fbb2e4c070344d18e65f1b3993867db")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation