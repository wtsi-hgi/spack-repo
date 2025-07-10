# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinesath1cdf(RPackage):
	"""tinesath1cdf

	A package containing an environment represeting the newcdf/tinesATH1.cdf.cdf file.
	"""
	
	bioc = "tinesath1cdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/tinesath1cdf_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/tinesath1cdf/tinesath1cdf_1.40.0.tar.gz"]

	version("1.40.0", sha256="9ac0104f108085dfe489d50874c29541d4cfca85c31dfcbae8f256ed0c2fab89")


