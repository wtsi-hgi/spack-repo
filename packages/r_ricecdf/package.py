# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRicecdf(RPackage):
	"""ricecdf

	A package containing an environment representing the Rice.cdf file.
	"""
	
	bioc = "ricecdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ricecdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ricecdf/ricecdf_2.18.0.tar.gz"]

	version("2.18.0", md5="51db6f51f4adcfb7f4940d07668db8b8")

	depends_on("r-annotationdbi", type=("build", "run"))

