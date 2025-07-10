# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RU133aaofav2cdf(RPackage):
	"""u133aaofav2cdf

	A package containing an environment representing the U133AAofAv2.CDF file.
	"""
	
	bioc = "u133aaofav2cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/u133aaofav2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/u133aaofav2cdf/u133aaofav2cdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="352b6cc801c64a7da19a207c12664288b60c718fa195ae1db80053ca29d15014")

	depends_on("r-annotationdbi", type=("build", "run"))

