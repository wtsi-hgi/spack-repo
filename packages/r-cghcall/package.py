# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghcall(RPackage):
	"""Calling aberrations for array CGH tumor profiles.

	Calls aberrations for array CGH data using a six state mixture model as well as several biological concepts that are ignored by existing algorithms. Visualization of profiles is also provided.
	"""
	
	bioc = "CGHcall" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CGHcall_2.64.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CGHcall/CGHcall_2.64.0.tar.gz"]

	version("2.64.0", md5="7a43fd6ae1e6c288b98abd2b8824fed4")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-impute@1.8:", type=("build", "run"))
	depends_on("r-dnacopy@1.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-cghbase@1.15.1:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
