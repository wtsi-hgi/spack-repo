# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH5vcdata(RPackage):
	"""Example data for the h5vc package

	This package contains the data used in the vignettes and examples of the 'h5vc' package
	"""
	
	bioc = "h5vcData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/h5vcData_2.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/h5vcData/h5vcData_2.22.0.tar.gz"]

	version("2.22.0", md5="c251316e2d6dc6cb90e8faad0015103b")


	# experiment