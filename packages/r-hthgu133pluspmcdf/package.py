# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133pluspmcdf(RPackage):
	"""hthgu133pluspmcdf

	A package containing an environment representing the HT_HG-U133_Plus_PM.CDF file.
	"""
	
	bioc = "hthgu133pluspmcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hthgu133pluspmcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hthgu133pluspmcdf/hthgu133pluspmcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="56d15101d59decac7811caa15b349a9c")

	depends_on("r-annotationdbi", type=("build", "run"))

