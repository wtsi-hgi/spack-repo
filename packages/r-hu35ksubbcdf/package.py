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

	version("2.18.0", md5="d873b6c521e926b331f799baf10a4e13")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation