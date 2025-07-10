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

	version("2.18.0", sha256="3e98e705639960638306b1537fb9f248af5e6764f3a01f5fd809e75727f5542f")

	depends_on("r-annotationdbi", type=("build", "run"))

