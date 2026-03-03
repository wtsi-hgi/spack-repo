# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVitisviniferacdf(RPackage):
	"""vitisviniferacdf

	A package containing an environment representing the Vitis_Vinifera.cdf file.
	"""
	
	bioc = "vitisviniferacdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/vitisviniferacdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/vitisviniferacdf/vitisviniferacdf_2.18.0.tar.gz"]

	version("2.18.0", md5="8eb491f3ffa3ff0814f5c155787ae160")

	depends_on("r-annotationdbi", type=("build", "run"))

