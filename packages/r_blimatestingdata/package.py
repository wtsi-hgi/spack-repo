# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlimatestingdata(RPackage):
	"""Data for testing of the package blima.

	Experiment data package. The set were prepared using microarray images of human mesenchymal cells treated with various supplements. This package is intended to provide example data to test functionality provided by blima.
	"""
	
	homepage = "https://bitbucket.org/kulvait/blima"
	bioc = "blimaTestingData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/blimaTestingData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/blimaTestingData/blimaTestingData_1.22.0.tar.gz"]

	version("1.22.0", md5="3ae3da97d0d020e16feee29b93c24825")

	depends_on("r@3:", type=("build", "run"))

