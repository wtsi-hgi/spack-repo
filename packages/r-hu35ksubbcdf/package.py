# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubbcdf(RPackage):
	"""hu35ksubbcdf

	A package containing an environment representing the Hu35KsubB.CDF file.
	"""
	
	bioc = "hu35ksubbcdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubbcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubbcdf/hu35ksubbcdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="556c0e112f0a26c66339c5748e954ecb27809e529d6fd2f0d8be3475ec82df2a")

	depends_on("r-annotationdbi", type=("build", "run"))

