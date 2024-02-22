# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRattoxfxcdf(RPackage):
	"""rattoxfxcdf

	A package containing an environment representing the RatToxFX.cdf file.
	"""
	
	bioc = "rattoxfxcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rattoxfxcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rattoxfxcdf/rattoxfxcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="912d0fa424615fcd92773ed174d5efdd")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation