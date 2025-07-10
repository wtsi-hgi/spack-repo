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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/medicagocdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/medicagocdf/medicagocdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="b8d8740ddc3e8054646e31352b72796bca082f1b694ac350ea0721c6d2319fb2")

	depends_on("r-annotationdbi", type=("build", "run"))

