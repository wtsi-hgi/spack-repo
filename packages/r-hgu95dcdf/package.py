# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95dcdf(RPackage):
	"""hgu95dcdf

	A package containing an environment representing the HG_U95D.CDF file.
	"""
	
	bioc = "hgu95dcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95dcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95dcdf/hgu95dcdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="80e14e2aaf5fb139c04a247f1f868a2fcebee96b710a6de18ad8696ce68ac068")

	depends_on("r-annotationdbi", type=("build", "run"))

